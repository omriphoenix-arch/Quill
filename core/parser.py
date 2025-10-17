"""
Parser for Quill
Builds an Abstract Syntax Tree (AST) from tokens
"""

from lexer import TokenType, Token

class ASTNode:
    """Base class for AST nodes with optional line/column tracking"""
    def __init__(self):
        self.line = 0
        self.column = 0
    
    def set_location(self, token):
        """Set location from a token"""
        if token:
            self.line = token.line
            self.column = token.column
        return self

class SayNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class AskNode(ASTNode):
    def __init__(self, prompt, variable):
        self.prompt = prompt
        self.variable = variable

class SetNode(ASTNode):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

class IfNode(ASTNode):
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

class ChoiceNode(ASTNode):
    def __init__(self, options):
        self.options = options

class GotoNode(ASTNode):
    def __init__(self, label):
        self.label = label

class LabelNode(ASTNode):
    def __init__(self, name):
        self.name = name

class BinaryOpNode(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class LiteralNode(ASTNode):
    def __init__(self, value):
        self.value = value

class VariableNode(ASTNode):
    def __init__(self, name):
        self.name = name

class WhileNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForNode(ASTNode):
    def __init__(self, variable, iterable, body):
        self.variable = variable
        self.iterable = iterable
        self.body = body

class FunctionNode(ASTNode):
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

class ReturnNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class FunctionCallNode(ASTNode):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

class ListNode(ASTNode):
    def __init__(self, elements):
        self.elements = elements

class IndexNode(ASTNode):
    def __init__(self, object, index):
        self.object = object
        self.index = index

class BreakNode(ASTNode):
    pass

class ContinueNode(ASTNode):
    pass

class UnaryOpNode(ASTNode):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

class ImportNode(ASTNode):
    def __init__(self, module_name, from_import=False, import_names=None):
        super().__init__()
        self.module_name = module_name
        self.from_import = from_import  # True for "from X import Y"
        self.import_names = import_names or []  # List of names to import, or ['*'] for wildcard

# GUI Nodes
class WindowNode(ASTNode):
    def __init__(self, title, properties=None):
        self.title = title
        self.properties = properties or {}

class ButtonNode(ASTNode):
    def __init__(self, text, properties=None):
        self.text = text
        self.properties = properties or {}

class TextboxNode(ASTNode):
    def __init__(self, text, properties=None):
        self.text = text
        self.properties = properties or {}

class ImageNode(ASTNode):
    def __init__(self, filepath, properties=None):
        self.filepath = filepath
        self.properties = properties or {}

class GUILabelNode(ASTNode):
    def __init__(self, text, properties=None):
        self.text = text
        self.properties = properties or {}

class InputNode(ASTNode):
    def __init__(self, variable, properties=None):
        self.variable = variable
        self.properties = properties or {}

class ShowNode(ASTNode):
    def __init__(self):
        pass

class HideNode(ASTNode):
    def __init__(self):
        pass

class UpdateNode(ASTNode):
    def __init__(self, widget_id, new_text):
        self.widget_id = widget_id
        self.new_text = new_text

class Parser:
    def __init__(self, tokens, source=""):
        self.tokens = tokens
        self.pos = 0
        self.source = source  # Store source for error context
    
    def current_token(self):
        if self.pos >= len(self.tokens):
            return self.tokens[-1]  # Return EOF
        return self.tokens[self.pos]
    
    def peek_token(self, offset=1):
        pos = self.pos + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[pos]
    
    def advance(self):
        self.pos += 1
    
    def expect(self, token_type):
        token = self.current_token()
        if token.type != token_type:
            from errors import QuillSyntaxError, get_hint
            source_lines = self.source.split('\n')
            source_line = source_lines[token.line - 1] if token.line <= len(source_lines) else ""
            error_msg = f"Expected {token_type.name}, got {token.type.name}"
            raise QuillSyntaxError(
                error_msg,
                line=token.line,
                column=token.column,
                source_line=source_line,
                hint=get_hint(error_msg)
            )
        self.advance()
        return token
    
    def skip_newlines(self):
        while self.current_token().type == TokenType.NEWLINE:
            self.advance()
    
    def parse(self):
        statements = []
        self.skip_newlines()
        
        while self.current_token().type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()
        
        return statements
    
    def parse_statement(self):
        token = self.current_token()
        
        if token.type == TokenType.SAY:
            return self.parse_say()
        elif token.type == TokenType.ASK:
            return self.parse_ask()
        elif token.type == TokenType.SET:
            return self.parse_set()
        elif token.type == TokenType.IF:
            return self.parse_if()
        elif token.type == TokenType.CHOICE:
            return self.parse_choice()
        elif token.type == TokenType.GOTO:
            return self.parse_goto()
        elif token.type == TokenType.LABEL:
            return self.parse_label()
        elif token.type == TokenType.WHILE:
            return self.parse_while()
        elif token.type == TokenType.FOR:
            return self.parse_for()
        elif token.type == TokenType.FUNCTION:
            return self.parse_function()
        elif token.type == TokenType.RETURN:
            return self.parse_return()
        elif token.type == TokenType.BREAK:
            self.advance()
            return BreakNode()
        elif token.type == TokenType.CONTINUE:
            self.advance()
            return ContinueNode()
        elif token.type == TokenType.IMPORT or token.type == TokenType.FROM:
            return self.parse_import()
        # GUI features commented out - uncomment to enable
        # elif token.type == TokenType.WINDOW:
        #     return self.parse_window()
        # elif token.type == TokenType.BUTTON:
        #     return self.parse_button()
        # elif token.type == TokenType.TEXTBOX:
        #     return self.parse_textbox()
        # elif token.type == TokenType.IMAGE:
        #     return self.parse_image()
        elif token.type == TokenType.LABEL:
            return self.parse_label()
        # elif token.type == TokenType.INPUT:
        #     return self.parse_input()
        # elif token.type == TokenType.SHOW:
        #     self.advance()
        #     return ShowNode()
        # elif token.type == TokenType.HIDE:
        #     self.advance()
        #     return HideNode()
        # elif token.type == TokenType.UPDATE:
        #     return self.parse_update()
        elif token.type == TokenType.IDENTIFIER:
            # Could be function call or assignment
            if self.peek_token().type == TokenType.LPAREN:
                return self.parse_function_call()
            elif self.peek_token().type == TokenType.ASSIGN:
                return self.parse_assignment()
            elif self.peek_token().type == TokenType.LBRACKET:
                return self.parse_index_assignment()
            else:
                raise SyntaxError(f"Unexpected identifier at line {token.line}")
        elif token.type == TokenType.NEWLINE:
            self.advance()
            return None
        else:
            raise SyntaxError(f"Unexpected token {token.type} at line {token.line}")
    
    def parse_say(self):
        self.expect(TokenType.SAY)
        expression = self.parse_expression()
        return SayNode(expression)
    
    def parse_ask(self):
        self.expect(TokenType.ASK)
        prompt = self.parse_expression()
        self.expect(TokenType.INTO)
        variable = self.expect(TokenType.IDENTIFIER).value
        return AskNode(prompt, variable)
    
    def parse_set(self):
        self.expect(TokenType.SET)
        variable = self.expect(TokenType.IDENTIFIER).value
        # Accept both 'to' and '='
        if self.current_token().type == TokenType.TO:
            self.advance()
        elif self.current_token().type == TokenType.ASSIGN:
            self.advance()
        else:
            raise SyntaxError(f"Expected 'to' or '=' after variable name at line {self.current_token().line}")
        expression = self.parse_expression()
        return SetNode(variable, expression)
    
    def parse_if(self):
        self.expect(TokenType.IF)
        condition = self.parse_expression()
        self.expect(TokenType.THEN)
        self.skip_newlines()
        
        then_block = []
        while self.current_token().type not in [TokenType.ELSE, TokenType.END, TokenType.EOF]:
            stmt = self.parse_statement()
            if stmt:
                then_block.append(stmt)
            self.skip_newlines()
        
        else_block = None
        if self.current_token().type == TokenType.ELSE:
            self.advance()
            self.skip_newlines()
            else_block = []
            while self.current_token().type not in [TokenType.END, TokenType.EOF]:
                stmt = self.parse_statement()
                if stmt:
                    else_block.append(stmt)
                self.skip_newlines()
        
        self.expect(TokenType.END)
        return IfNode(condition, then_block, else_block)
    
    def parse_choice(self):
        self.expect(TokenType.CHOICE)
        options = []
        
        # Parse first option (use parse_comparison to avoid logical or)
        option = self.parse_comparison()
        options.append(option)
        
        # Parse additional options separated by 'or'
        while self.current_token().type == TokenType.OR:
            self.advance()
            option = self.parse_comparison()
            options.append(option)
        
        return ChoiceNode(options)
    
    def parse_goto(self):
        self.expect(TokenType.GOTO)
        label = self.expect(TokenType.IDENTIFIER).value
        return GotoNode(label)
    
    def parse_label(self):
        self.expect(TokenType.LABEL)
        # Check if it's a goto label (label: name) or GUI label (label "text" ...)
        if self.current_token().type == TokenType.COLON:
            # Goto label
            self.expect(TokenType.COLON)
            name = self.expect(TokenType.IDENTIFIER).value
            return LabelNode(name)
        else:
            # GUI label
            text = self.parse_expression()
            properties = {}
            
            while self.current_token().type in [TokenType.AT, TokenType.COLOR, TokenType.SIZE, 
                                                 TokenType.FONT, TokenType.BGCOLOR]:
                if self.current_token().type == TokenType.AT:
                    self.advance()
                    x = self.parse_expression()
                    if self.current_token().type == TokenType.COMMA:
                        self.advance()
                    y = self.parse_expression()
                    properties['x'] = x
                    properties['y'] = y
                elif self.current_token().type == TokenType.COLOR:
                    self.advance()
                    properties['color'] = self.parse_expression()
                elif self.current_token().type == TokenType.BGCOLOR:
                    self.advance()
                    properties['bgcolor'] = self.parse_expression()
                elif self.current_token().type == TokenType.SIZE:
                    self.advance()
                    properties['size'] = self.parse_expression()
                elif self.current_token().type == TokenType.FONT:
                    self.advance()
                    properties['font'] = self.parse_expression()
            
            return GUILabelNode(text, properties)
    
    def parse_while(self):
        self.expect(TokenType.WHILE)
        condition = self.parse_expression()
        self.expect(TokenType.DO)
        self.skip_newlines()
        
        body = []
        while self.current_token().type not in [TokenType.END, TokenType.EOF]:
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
            self.skip_newlines()
        
        self.expect(TokenType.END)
        return WhileNode(condition, body)
    
    def parse_for(self):
        self.expect(TokenType.FOR)
        variable = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.IN)
        iterable = self.parse_expression()
        self.expect(TokenType.DO)
        self.skip_newlines()
        
        body = []
        while self.current_token().type not in [TokenType.END, TokenType.EOF]:
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
            self.skip_newlines()
        
        self.expect(TokenType.END)
        return ForNode(variable, iterable, body)
    
    def parse_function(self):
        self.expect(TokenType.FUNCTION)
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.LPAREN)
        
        parameters = []
        if self.current_token().type != TokenType.RPAREN:
            parameters.append(self.expect(TokenType.IDENTIFIER).value)
            while self.current_token().type == TokenType.COMMA:
                self.advance()
                parameters.append(self.expect(TokenType.IDENTIFIER).value)
        
        self.expect(TokenType.RPAREN)
        self.skip_newlines()
        
        body = []
        while self.current_token().type not in [TokenType.END, TokenType.EOF]:
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
            self.skip_newlines()
        
        self.expect(TokenType.END)
        return FunctionNode(name, parameters, body)
    
    def parse_return(self):
        self.expect(TokenType.RETURN)
        if self.current_token().type in [TokenType.NEWLINE, TokenType.EOF]:
            return ReturnNode(None)
        expression = self.parse_expression()
        return ReturnNode(expression)
    
    def parse_import(self):
        """
        Parse import statements:
        - import module_name
        - from module_name import function1, function2
        - from module_name import *
        """
        token = self.current_token()
        
        # Check if it's "from X import Y" or just "import X"
        if token.type == TokenType.FROM:
            # from module_name import ...
            self.advance()  # consume 'from'
            module_name = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.IMPORT)
            
            # Parse import names
            import_names = []
            if self.current_token().type == TokenType.MULTIPLY:  # * for wildcard
                self.advance()
                import_names = ['*']
            else:
                import_names.append(self.expect(TokenType.IDENTIFIER).value)
                while self.current_token().type == TokenType.COMMA:
                    self.advance()
                    import_names.append(self.expect(TokenType.IDENTIFIER).value)
            
            node = ImportNode(module_name, from_import=True, import_names=import_names)
            node.set_location(token)
            return node
        else:
            # import module_name
            self.expect(TokenType.IMPORT)
            module_name = self.expect(TokenType.IDENTIFIER).value
            node = ImportNode(module_name, from_import=False)
            node.set_location(token)
            return node
    
    def parse_function_call(self):
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.LPAREN)
        
        arguments = []
        if self.current_token().type != TokenType.RPAREN:
            arguments.append(self.parse_expression())
            while self.current_token().type == TokenType.COMMA:
                self.advance()
                arguments.append(self.parse_expression())
        
        self.expect(TokenType.RPAREN)
        return FunctionCallNode(name, arguments)
    
    def parse_assignment(self):
        variable = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.ASSIGN)
        expression = self.parse_expression()
        return SetNode(variable, expression)
    
    def parse_index_assignment(self):
        variable = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.LBRACKET)
        index = self.parse_expression()
        self.expect(TokenType.RBRACKET)
        self.expect(TokenType.ASSIGN)
        value = self.parse_expression()
        
        # Create a special node for index assignment
        index_node = IndexNode(VariableNode(variable), index)
        return SetNode(index_node, value)
    
    def parse_expression(self):
        return self.parse_logical_or()
    
    def parse_logical_or(self):
        left = self.parse_logical_and()
        
        while self.current_token().type == TokenType.OR:
            self.advance()
            right = self.parse_logical_and()
            left = BinaryOpNode(left, 'or', right)
        
        return left
    
    def parse_logical_and(self):
        left = self.parse_comparison()
        
        while self.current_token().type == TokenType.AND:
            self.advance()
            right = self.parse_comparison()
            left = BinaryOpNode(left, 'and', right)
        
        return left
    
    def parse_comparison(self):
        left = self.parse_addition()
        
        while self.current_token().type in [TokenType.EQUALS, TokenType.NOT_EQUALS, 
                                            TokenType.GREATER, TokenType.LESS,
                                            TokenType.GREATER_EQUAL, TokenType.LESS_EQUAL,
                                            TokenType.IS]:
            if self.current_token().type == TokenType.EQUALS:
                self.advance()
                right = self.parse_addition()
                left = BinaryOpNode(left, '==', right)
            elif self.current_token().type == TokenType.NOT_EQUALS:
                self.advance()
                right = self.parse_addition()
                left = BinaryOpNode(left, '!=', right)
            elif self.current_token().type == TokenType.GREATER:
                self.advance()
                right = self.parse_addition()
                left = BinaryOpNode(left, '>', right)
            elif self.current_token().type == TokenType.LESS:
                self.advance()
                right = self.parse_addition()
                left = BinaryOpNode(left, '<', right)
            elif self.current_token().type == TokenType.GREATER_EQUAL:
                self.advance()
                right = self.parse_addition()
                left = BinaryOpNode(left, '>=', right)
            elif self.current_token().type == TokenType.LESS_EQUAL:
                self.advance()
                right = self.parse_addition()
                left = BinaryOpNode(left, '<=', right)
            elif self.current_token().type == TokenType.IS:
                self.advance()
                right = self.parse_addition()
                left = BinaryOpNode(left, '==', right)
        
        return left
    
    def parse_addition(self):
        left = self.parse_multiplication()
        
        while self.current_token().type in [TokenType.PLUS, TokenType.MINUS]:
            if self.current_token().type == TokenType.PLUS:
                self.advance()
                right = self.parse_multiplication()
                left = BinaryOpNode(left, '+', right)
            elif self.current_token().type == TokenType.MINUS:
                self.advance()
                right = self.parse_multiplication()
                left = BinaryOpNode(left, '-', right)
        
        return left
    
    def parse_multiplication(self):
        left = self.parse_power()
        
        while self.current_token().type in [TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO]:
            if self.current_token().type == TokenType.MULTIPLY:
                self.advance()
                right = self.parse_power()
                left = BinaryOpNode(left, '*', right)
            elif self.current_token().type == TokenType.DIVIDE:
                op_token = self.current_token()
                self.advance()
                right = self.parse_power()
                left = BinaryOpNode(left, '/', right).set_location(op_token)
            elif self.current_token().type == TokenType.MODULO:
                self.advance()
                right = self.parse_power()
                left = BinaryOpNode(left, '%', right)
        
        return left
    
    def parse_power(self):
        left = self.parse_unary()
        
        if self.current_token().type == TokenType.POWER:
            self.advance()
            right = self.parse_power()  # Right associative
            left = BinaryOpNode(left, '**', right)
        
        return left
    
    def parse_unary(self):
        if self.current_token().type == TokenType.NOT:
            self.advance()
            operand = self.parse_unary()
            return UnaryOpNode('not', operand)
        elif self.current_token().type == TokenType.MINUS:
            self.advance()
            operand = self.parse_unary()
            return UnaryOpNode('-', operand)
        
        return self.parse_postfix()
    
    def parse_postfix(self):
        expr = self.parse_term()
        
        while True:
            if self.current_token().type == TokenType.LBRACKET:
                self.advance()
                index = self.parse_expression()
                self.expect(TokenType.RBRACKET)
                expr = IndexNode(expr, index)
            elif self.current_token().type == TokenType.LPAREN:
                # Function call
                self.advance()
                arguments = []
                if self.current_token().type != TokenType.RPAREN:
                    arguments.append(self.parse_expression())
                    while self.current_token().type == TokenType.COMMA:
                        self.advance()
                        arguments.append(self.parse_expression())
                self.expect(TokenType.RPAREN)
                
                if isinstance(expr, VariableNode):
                    expr = FunctionCallNode(expr.name, arguments)
                else:
                    raise SyntaxError(f"Cannot call non-function at line {self.current_token().line}")
            else:
                break
        
        return expr
    
    def parse_term(self):
        token = self.current_token()
        
        if token.type == TokenType.STRING:
            self.advance()
            return LiteralNode(token.value)
        elif token.type == TokenType.NUMBER:
            self.advance()
            return LiteralNode(token.value)
        elif token.type == TokenType.TRUE:
            self.advance()
            return LiteralNode(True)
        elif token.type == TokenType.FALSE:
            self.advance()
            return LiteralNode(False)
        elif token.type == TokenType.NULL:
            self.advance()
            return LiteralNode(None)
        elif token.type == TokenType.LBRACKET:
            return self.parse_list()
        elif token.type == TokenType.LPAREN:
            self.advance()
            expr = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return expr
        elif token.type == TokenType.IDENTIFIER:
            self.advance()
            return VariableNode(token.value).set_location(token)
        else:
            raise SyntaxError(f"Unexpected token {token.type} at line {token.line}")
    
    def parse_list(self):
        self.expect(TokenType.LBRACKET)
        elements = []
        
        if self.current_token().type != TokenType.RBRACKET:
            elements.append(self.parse_expression())
            while self.current_token().type == TokenType.COMMA:
                self.advance()
                if self.current_token().type == TokenType.RBRACKET:
                    break
                elements.append(self.parse_expression())
        
        self.expect(TokenType.RBRACKET)
        return ListNode(elements)
    
    # GUI Parsing Methods
    def parse_window(self):
        """Parse: window "Title" size 800x600 theme dark bgcolor #282828"""
        self.expect(TokenType.WINDOW)
        title = self.parse_expression()
        properties = {}
        
        while self.current_token().type in [TokenType.SIZE, TokenType.THEME, TokenType.BGCOLOR, 
                                             TokenType.WIDTH, TokenType.HEIGHT]:
            if self.current_token().type == TokenType.SIZE:
                self.advance()
                properties['size'] = self.parse_expression()
            elif self.current_token().type == TokenType.WIDTH:
                self.advance()
                properties['width'] = self.parse_expression()
            elif self.current_token().type == TokenType.HEIGHT:
                self.advance()
                properties['height'] = self.parse_expression()
            elif self.current_token().type == TokenType.THEME:
                self.advance()
                # Theme is typically an identifier (dark, light, game)
                if self.current_token().type == TokenType.IDENTIFIER:
                    properties['theme'] = self.current_token().value
                    self.advance()
                else:
                    properties['theme'] = self.parse_expression()
            elif self.current_token().type == TokenType.BGCOLOR:
                self.advance()
                properties['bgcolor'] = self.parse_expression()
        
        return WindowNode(title, properties)
    
    def parse_button(self):
        """Parse: button "Click Me" at 100,50 color blue onclick my_function"""
        self.expect(TokenType.BUTTON)
        text = self.parse_expression()
        properties = {}
        
        while self.current_token().type in [TokenType.AT, TokenType.COLOR, TokenType.SIZE, 
                                             TokenType.ONCLICK, TokenType.WIDTH, TokenType.HEIGHT,
                                             TokenType.BGCOLOR, TokenType.FONT]:
            if self.current_token().type == TokenType.AT:
                self.advance()
                # Parse x coordinate
                x = self.parse_expression()
                if self.current_token().type == TokenType.COMMA:
                    self.advance()
                # Parse y coordinate
                y = self.parse_expression()
                properties['x'] = x
                properties['y'] = y
            elif self.current_token().type == TokenType.COLOR:
                self.advance()
                properties['color'] = self.parse_expression()
            elif self.current_token().type == TokenType.BGCOLOR:
                self.advance()
                properties['bgcolor'] = self.parse_expression()
            elif self.current_token().type == TokenType.SIZE:
                self.advance()
                properties['size'] = self.parse_expression()
            elif self.current_token().type == TokenType.FONT:
                self.advance()
                properties['font'] = self.parse_expression()
            elif self.current_token().type == TokenType.WIDTH:
                self.advance()
                properties['width'] = self.parse_expression()
            elif self.current_token().type == TokenType.HEIGHT:
                self.advance()
                properties['height'] = self.parse_expression()
            elif self.current_token().type == TokenType.ONCLICK:
                self.advance()
                # Get the identifier name for the callback function
                if self.current_token().type == TokenType.IDENTIFIER:
                    properties['onclick'] = self.current_token().value
                    self.advance()
                else:
                    raise SyntaxError(f"Expected identifier after 'onclick' at line {self.current_token().line}")
        
        return ButtonNode(text, properties)
    
    def parse_textbox(self):
        """Parse: textbox "Welcome!" at 100,50 color gold size 24 font Arial"""
        self.expect(TokenType.TEXTBOX)
        text = self.parse_expression()
        properties = {}
        
        while self.current_token().type in [TokenType.AT, TokenType.COLOR, TokenType.SIZE, 
                                             TokenType.FONT, TokenType.ALIGN, TokenType.BGCOLOR, TokenType.ID]:
            if self.current_token().type == TokenType.AT:
                self.advance()
                x = self.parse_expression()
                if self.current_token().type == TokenType.COMMA:
                    self.advance()
                y = self.parse_expression()
                properties['x'] = x
                properties['y'] = y
            elif self.current_token().type == TokenType.COLOR:
                self.advance()
                properties['color'] = self.parse_expression()
            elif self.current_token().type == TokenType.BGCOLOR:
                self.advance()
                properties['bgcolor'] = self.parse_expression()
            elif self.current_token().type == TokenType.SIZE:
                self.advance()
                properties['size'] = self.parse_expression()
            elif self.current_token().type == TokenType.FONT:
                self.advance()
                properties['font'] = self.parse_expression()
            elif self.current_token().type == TokenType.ALIGN:
                self.advance()
                properties['align'] = self.current_token().value
                self.advance()
            elif self.current_token().type == TokenType.ID:
                self.advance()
                if self.current_token().type == TokenType.IDENTIFIER:
                    properties['id'] = self.current_token().value
                    self.advance()
                else:
                    raise SyntaxError(f"Expected identifier after 'id' at line {self.current_token().line}")
        
        return TextboxNode(text, properties)
    
    def parse_image(self):
        """Parse: image "background.png" at 0,0 width 800 height 600"""
        self.expect(TokenType.IMAGE)
        filepath = self.parse_expression()
        properties = {}
        
        while self.current_token().type in [TokenType.AT, TokenType.WIDTH, TokenType.HEIGHT, TokenType.SIZE]:
            if self.current_token().type == TokenType.AT:
                self.advance()
                x = self.parse_expression()
                if self.current_token().type == TokenType.COMMA:
                    self.advance()
                y = self.parse_expression()
                properties['x'] = x
                properties['y'] = y
            elif self.current_token().type == TokenType.WIDTH:
                self.advance()
                properties['width'] = self.parse_expression()
            elif self.current_token().type == TokenType.HEIGHT:
                self.advance()
                properties['height'] = self.parse_expression()
            elif self.current_token().type == TokenType.SIZE:
                self.advance()
                properties['size'] = self.parse_expression()
        
        return ImageNode(filepath, properties)
    
    def parse_input(self):
        """Parse: input username at 100,100 width 200"""
        self.expect(TokenType.INPUT)
        variable = self.expect(TokenType.IDENTIFIER).value
        properties = {}
        
        while self.current_token().type in [TokenType.AT, TokenType.WIDTH, TokenType.HEIGHT, 
                                             TokenType.COLOR, TokenType.BGCOLOR, TokenType.FONT, TokenType.SIZE]:
            if self.current_token().type == TokenType.AT:
                self.advance()
                x = self.parse_expression()
                if self.current_token().type == TokenType.COMMA:
                    self.advance()
                y = self.parse_expression()
                properties['x'] = x
                properties['y'] = y
            elif self.current_token().type == TokenType.WIDTH:
                self.advance()
                properties['width'] = self.parse_expression()
            elif self.current_token().type == TokenType.HEIGHT:
                self.advance()
                properties['height'] = self.parse_expression()
            elif self.current_token().type == TokenType.COLOR:
                self.advance()
                properties['color'] = self.parse_expression()
            elif self.current_token().type == TokenType.BGCOLOR:
                self.advance()
                properties['bgcolor'] = self.parse_expression()
            elif self.current_token().type == TokenType.FONT:
                self.advance()
                properties['font'] = self.parse_expression()
            elif self.current_token().type == TokenType.SIZE:
                self.advance()
                properties['size'] = self.parse_expression()
        
        return InputNode(variable, properties)
    
    def parse_update(self):
        """Parse: update score_display to "Score: 50" """
        self.expect(TokenType.UPDATE)
        widget_id = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.TO)
        new_text = self.parse_expression()
        return UpdateNode(widget_id, new_text)
