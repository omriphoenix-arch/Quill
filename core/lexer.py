"""
Lexer (Tokenizer) for StoryScript
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
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line
    
    def __repr__(self):
        return f"Token({self.type}, {self.value}, line {self.line})"

class Lexer:
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.line = 1
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
            'from': TokenType.IN,
            
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
        self.pos += 1
    
    def skip_whitespace(self):
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def skip_comment(self):
        if self.current_char() == '#':
            while self.current_char() and self.current_char() != '\n':
                self.advance()
    
    def read_string(self):
        quote_char = self.current_char()
        self.advance()  # Skip opening quote
        
        value = ''
        while self.current_char() and self.current_char() != quote_char:
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
            raise SyntaxError(f"Unterminated string at line {self.line}")
        
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
                self.tokens.append(Token(TokenType.NEWLINE, '\n', self.line))
                self.advance()
                continue
            
            # Strings
            if self.current_char() in '"\'':
                value = self.read_string()
                self.tokens.append(Token(TokenType.STRING, value, self.line))
                continue
            
            # Numbers
            if self.current_char().isdigit():
                value = self.read_number()
                self.tokens.append(Token(TokenType.NUMBER, value, self.line))
                continue
            
            # Operators and punctuation
            if self.current_char() == '+':
                self.tokens.append(Token(TokenType.PLUS, '+', self.line))
                self.advance()
                continue
            
            if self.current_char() == '-':
                self.tokens.append(Token(TokenType.MINUS, '-', self.line))
                self.advance()
                continue
            
            if self.current_char() == '*':
                if self.peek_char() == '*':
                    self.tokens.append(Token(TokenType.POWER, '**', self.line))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.MULTIPLY, '*', self.line))
                    self.advance()
                continue
            
            if self.current_char() == '/':
                self.tokens.append(Token(TokenType.DIVIDE, '/', self.line))
                self.advance()
                continue
            
            if self.current_char() == '%':
                self.tokens.append(Token(TokenType.MODULO, '%', self.line))
                self.advance()
                continue
            
            if self.current_char() == '=':
                if self.peek_char() == '=':
                    self.tokens.append(Token(TokenType.EQUALS, '==', self.line))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.ASSIGN, '=', self.line))
                    self.advance()
                continue
            
            if self.current_char() == '!':
                if self.peek_char() == '=':
                    self.tokens.append(Token(TokenType.NOT_EQUALS, '!=', self.line))
                    self.advance()
                    self.advance()
                    continue
            
            if self.current_char() == '>':
                if self.peek_char() == '=':
                    self.tokens.append(Token(TokenType.GREATER_EQUAL, '>=', self.line))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.GREATER, '>', self.line))
                    self.advance()
                continue
            
            if self.current_char() == '<':
                if self.peek_char() == '=':
                    self.tokens.append(Token(TokenType.LESS_EQUAL, '<=', self.line))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.LESS, '<', self.line))
                    self.advance()
                continue
            
            if self.current_char() == ':':
                self.tokens.append(Token(TokenType.COLON, ':', self.line))
                self.advance()
                continue
            
            if self.current_char() == ',':
                self.tokens.append(Token(TokenType.COMMA, ',', self.line))
                self.advance()
                continue
            
            if self.current_char() == '(':
                self.tokens.append(Token(TokenType.LPAREN, '(', self.line))
                self.advance()
                continue
            
            if self.current_char() == ')':
                self.tokens.append(Token(TokenType.RPAREN, ')', self.line))
                self.advance()
                continue
            
            if self.current_char() == '[':
                self.tokens.append(Token(TokenType.LBRACKET, '[', self.line))
                self.advance()
                continue
            
            if self.current_char() == ']':
                self.tokens.append(Token(TokenType.RBRACKET, ']', self.line))
                self.advance()
                continue
            
            if self.current_char() == '.':
                self.tokens.append(Token(TokenType.DOT, '.', self.line))
                self.advance()
                continue
            
            # Identifiers and keywords
            if self.current_char().isalpha() or self.current_char() == '_':
                value = self.read_identifier()
                token_type = self.keywords.get(value.lower(), TokenType.IDENTIFIER)
                self.tokens.append(Token(token_type, value, self.line))
                continue
            
            raise SyntaxError(f"Unknown character '{self.current_char()}' at line {self.line}")
        
        self.tokens.append(Token(TokenType.EOF, None, self.line))
        return self.tokens
