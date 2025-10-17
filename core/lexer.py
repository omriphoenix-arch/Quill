"""
Lexer (Tokenizer) for Quill
Breaks source code into tokens
"""

import re
from enum import Enum, auto

class TokenType(Enum):
    # Keywords
    SAY = auto()
    ASK = auto()
    INTO = auto()
    SET = auto()
    TO = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    ELSIF = auto()
    END = auto()
    CHOICE = auto()
    OR = auto()
    GOTO = auto()
    LABEL = auto()
    IS = auto()
    WHILE = auto()
    DO = auto()
    FOR = auto()
    IN = auto()
    FUNCTION = auto()
    RETURN = auto()
    AND = auto()
    NOT = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    BREAK = auto()
    CONTINUE = auto()
    IMPORT = auto()
    FROM = auto()
    
    # GUI Keywords (Optional - uncomment if using GUI features)
    # WINDOW = auto()
    # BUTTON = auto()
    # TEXTBOX = auto()
    # IMAGE = auto()
    # INPUT = auto()
    # THEME = auto()
    # COLOR = auto()
    # SIZE = auto()
    # AT = auto()
    # ONCLICK = auto()
    # SHOW = auto()
    # HIDE = auto()
    # BGCOLOR = auto()
    # FONT = auto()
    # STYLE = auto()
    # WIDTH = auto()
    # HEIGHT = auto()
    # ALIGN = auto()
    # ID = auto()
    # UPDATE = auto()
    
    # Operators
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    MODULO = auto()
    POWER = auto()
    EQUALS = auto()
    NOT_EQUALS = auto()
    GREATER = auto()
    LESS = auto()
    GREATER_EQUAL = auto()
    LESS_EQUAL = auto()
    ASSIGN = auto()
    
    # Literals
    STRING = auto()
    NUMBER = auto()
    IDENTIFIER = auto()
    
    # Special
    NEWLINE = auto()
    EOF = auto()
    COLON = auto()
    COMMA = auto()
    LPAREN = auto()
    RPAREN = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    DOT = auto()

class Token:
    def __init__(self, type, value, line, column=0):
        self.type = type
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type}, {self.value}, line {self.line}, col {self.column})"

class Lexer:
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.line_start_pos = 0  # Track start of current line for column calculation
        self.tokens = []
        
        # Keywords mapping
        self.keywords = {
            # Output commands
            'say': TokenType.SAY,
            'print': TokenType.SAY,
            'speak': TokenType.SAY,
            'tell': TokenType.SAY,
            'write': TokenType.SAY,
            
            # Input commands
            'ask': TokenType.ASK,
            'prompt': TokenType.ASK,
            
            # Connectors
            'into': TokenType.INTO,
            'in': TokenType.IN,
            'from': TokenType.FROM,
            
            # Variables
            'set': TokenType.SET,
            'let': TokenType.SET,
            'make': TokenType.SET,
            'create': TokenType.SET,
            'to': TokenType.TO,
            'equals': TokenType.TO,
            
            # Conditionals
            'if': TokenType.IF,
            'when': TokenType.IF,
            'then': TokenType.THEN,
            'else': TokenType.ELSE,
            'otherwise': TokenType.ELSE,
            'elsif': TokenType.ELSIF,
            'elif': TokenType.ELSIF,
            'elseif': TokenType.ELSIF,
            'end': TokenType.END,
            'done': TokenType.END,
            'finish': TokenType.END,
            
            # Choices
            'choice': TokenType.CHOICE,
            # Note: 'choose', 'select', 'option' removed as keywords to allow as variable names
            'or': TokenType.OR,
            
            # Navigation
            'goto': TokenType.GOTO,
            'jump': TokenType.GOTO,
            'go': TokenType.GOTO,
            'label': TokenType.LABEL,
            
            # Comparison
            'is': TokenType.IS,
            'equals': TokenType.IS,
            
            # Loops
            'while': TokenType.WHILE,
            'repeat': TokenType.WHILE,
            'do': TokenType.DO,
            'for': TokenType.FOR,
            'each': TokenType.FOR,
            
            # Functions
            'function': TokenType.FUNCTION,
            'func': TokenType.FUNCTION,
            'def': TokenType.FUNCTION,
            'define': TokenType.FUNCTION,
            'return': TokenType.RETURN,
            'give': TokenType.RETURN,
            
            # Logic
            'and': TokenType.AND,
            'not': TokenType.NOT,
            'true': TokenType.TRUE,
            'false': TokenType.FALSE,
            'null': TokenType.NULL,
            'none': TokenType.NULL,
            'break': TokenType.BREAK,
            'continue': TokenType.CONTINUE,
            'import': TokenType.IMPORT,
            
            # GUI keywords (commented out - uncomment if using GUI features)
            # 'window': TokenType.WINDOW,
            # 'screen': TokenType.WINDOW,
            # 'button': TokenType.BUTTON,
            # 'btn': TokenType.BUTTON,
            # 'textbox': TokenType.TEXTBOX,
            # 'text': TokenType.TEXTBOX,
            # 'image': TokenType.IMAGE,
            # 'img': TokenType.IMAGE,
            # 'picture': TokenType.IMAGE,
            # 'input': TokenType.INPUT,
            # 'textfield': TokenType.INPUT,
            # 'field': TokenType.INPUT,
            # 'theme': TokenType.THEME,
            # 'color': TokenType.COLOR,
            # 'colour': TokenType.COLOR,
            # 'foreground': TokenType.COLOR,
            # 'size': TokenType.SIZE,
            # 'at': TokenType.AT,
            # 'position': TokenType.AT,
            # 'pos': TokenType.AT,
            # 'onclick': TokenType.ONCLICK,
            # 'click': TokenType.ONCLICK,
            # 'press': TokenType.ONCLICK,
            # 'show': TokenType.SHOW,
            # 'display': TokenType.SHOW,
            # 'open': TokenType.SHOW,
            # 'hide': TokenType.HIDE,
            # 'close': TokenType.HIDE,
            # 'bgcolor': TokenType.BGCOLOR,
            # 'background': TokenType.BGCOLOR,
            # 'bg': TokenType.BGCOLOR,
            # 'font': TokenType.FONT,
            # 'typeface': TokenType.FONT,
            # 'style': TokenType.STYLE,
            # 'width': TokenType.WIDTH,
            # 'height': TokenType.HEIGHT,
            # 'align': TokenType.ALIGN,
            # 'alignment': TokenType.ALIGN,
            # 'id': TokenType.ID,
            # 'name': TokenType.ID,
            # 'update': TokenType.UPDATE,
            # 'change': TokenType.UPDATE,
            # 'modify': TokenType.UPDATE,
        }
    
    def current_char(self):
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]
    
    def peek_char(self, offset=1):
        pos = self.pos + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self):
        if self.pos < len(self.source) and self.source[self.pos] == '\n':
            self.line += 1
            self.line_start_pos = self.pos + 1
            self.column = 1
        else:
            self.column += 1
        self.pos += 1
    
    def skip_whitespace(self):
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def skip_comment(self):
        if self.current_char() == '#':
            while self.current_char() and self.current_char() != '\n':
                self.advance()
    
    def get_column(self):
        """Get current column (1-indexed)"""
        return self.pos - self.line_start_pos + 1
    
    def add_token(self, token_type, value):
        """Helper to add a token with current line and column"""
        self.tokens.append(Token(token_type, value, self.line, self.get_column()))
    
    def read_string(self):
        start_line = self.line
        start_col = self.get_column()
        quote_char = self.current_char()
        self.advance()  # Skip opening quote
        
        value = ''
        while self.current_char() and self.current_char() != quote_char:
            # Strings cannot span multiple lines in Quill
            if self.current_char() == '\n':
                from errors import QuillSyntaxError, COMMON_HINTS
                source_lines = self.source.split('\n')
                source_line = source_lines[start_line - 1] if start_line <= len(source_lines) else ""
                raise QuillSyntaxError(
                    f"Unterminated string starting at column {start_col}",
                    line=start_line,
                    column=start_col,
                    source_line=source_line,
                    hint=COMMON_HINTS["unterminated_string"]
                )
            
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() == 'n':
                    value += '\n'
                elif self.current_char() == 't':
                    value += '\t'
                elif self.current_char():
                    value += self.current_char()
                self.advance()
            else:
                value += self.current_char()
                self.advance()
        
        if self.current_char() == quote_char:
            self.advance()  # Skip closing quote
        else:
            from errors import QuillSyntaxError, COMMON_HINTS
            source_lines = self.source.split('\n')
            source_line = source_lines[start_line - 1] if start_line <= len(source_lines) else ""
            raise QuillSyntaxError(
                f"Unterminated string (reached end of file)",
                line=start_line,
                column=start_col,
                source_line=source_line,
                hint=COMMON_HINTS["unterminated_string"]
            )
        
        return value
    
    def read_number(self):
        value = ''
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            value += self.current_char()
            self.advance()
        return float(value) if '.' in value else int(value)
    
    def read_identifier(self):
        value = ''
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            value += self.current_char()
            self.advance()
        return value
    
    def tokenize(self):
        while self.pos < len(self.source):
            self.skip_whitespace()
            
            if not self.current_char():
                break
            
            # Comments
            if self.current_char() == '#':
                self.skip_comment()
                continue
            
            # Newlines
            if self.current_char() == '\n':
                self.add_token(TokenType.NEWLINE, '\n')
                self.advance()
                continue
            
            # Strings
            if self.current_char() in '"\'':
                value = self.read_string()
                self.add_token(TokenType.STRING, value)
                continue
            
            # Numbers
            if self.current_char().isdigit():
                value = self.read_number()
                self.add_token(TokenType.NUMBER, value)
                continue
            
            # Operators and punctuation
            if self.current_char() == '+':
                self.add_token(TokenType.PLUS, '+')
                self.advance()
                continue
            
            if self.current_char() == '-':
                self.add_token(TokenType.MINUS, '-')
                self.advance()
                continue
            
            if self.current_char() == '*':
                if self.peek_char() == '*':
                    self.add_token(TokenType.POWER, '**')
                    self.advance()
                    self.advance()
                else:
                    self.add_token(TokenType.MULTIPLY, '*')
                    self.advance()
                continue
            
            if self.current_char() == '/':
                self.add_token(TokenType.DIVIDE, '/')
                self.advance()
                continue
            
            if self.current_char() == '%':
                self.add_token(TokenType.MODULO, '%')
                self.advance()
                continue
            
            if self.current_char() == '=':
                if self.peek_char() == '=':
                    self.add_token(TokenType.EQUALS, '==')
                    self.advance()
                    self.advance()
                else:
                    self.add_token(TokenType.ASSIGN, '=')
                    self.advance()
                continue
            
            if self.current_char() == '!':
                if self.peek_char() == '=':
                    self.add_token(TokenType.NOT_EQUALS, '!=')
                    self.advance()
                    self.advance()
                    continue
            
            if self.current_char() == '>':
                if self.peek_char() == '=':
                    self.add_token(TokenType.GREATER_EQUAL, '>=')
                    self.advance()
                    self.advance()
                else:
                    self.add_token(TokenType.GREATER, '>')
                    self.advance()
                continue
            
            if self.current_char() == '<':
                if self.peek_char() == '=':
                    self.add_token(TokenType.LESS_EQUAL, '<=')
                    self.advance()
                    self.advance()
                else:
                    self.add_token(TokenType.LESS, '<')
                    self.advance()
                continue
            
            if self.current_char() == ':':
                self.add_token(TokenType.COLON, ':')
                self.advance()
                continue
            
            if self.current_char() == ',':
                self.add_token(TokenType.COMMA, ',')
                self.advance()
                continue
            
            if self.current_char() == '(':
                self.add_token(TokenType.LPAREN, '(')
                self.advance()
                continue
            
            if self.current_char() == ')':
                self.add_token(TokenType.RPAREN, ')')
                self.advance()
                continue
            
            if self.current_char() == '[':
                self.add_token(TokenType.LBRACKET, '[')
                self.advance()
                continue
            
            if self.current_char() == ']':
                self.add_token(TokenType.RBRACKET, ']')
                self.advance()
                continue
            
            if self.current_char() == '.':
                self.add_token(TokenType.DOT, '.')
                self.advance()
                continue
            
            # Identifiers and keywords
            if self.current_char().isalpha() or self.current_char() == '_':
                value = self.read_identifier()
                token_type = self.keywords.get(value.lower(), TokenType.IDENTIFIER)
                self.add_token(token_type, value)
                continue
            
            # Unknown character error
            from errors import QuillSyntaxError
            source_lines = self.source.split('\n')
            source_line = source_lines[self.line - 1] if self.line <= len(source_lines) else ""
            raise QuillSyntaxError(
                f"Unknown character '{self.current_char()}'",
                line=self.line,
                column=self.get_column(),
                source_line=source_line,
                hint="Check for typos or unsupported characters"
            )
        
        self.add_token(TokenType.EOF, None)
        return self.tokens
