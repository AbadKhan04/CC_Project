class Parser:
    def __init__(self, tokens, variables):
        self.tokens = tokens
        self.variables = variables
        self.current_token = None
        self.peek_index = 0

    def advance(self):
        self.peek_index += 1
        if self.peek_index < len(self.tokens):
            self.current_token = self.tokens[self.peek_index]
        else:
            self.current_token = None

    def parse(self):
        while self.peek_index < len(self.tokens):
            token_type, value = self.tokens[self.peek_index]
            if token_type == "VAR":
                self.parse_variable_declaration()
            elif token_type == "ADD":
                self.parse_addition()
            elif token_type == "SUB":
                self.parse_subtraction()
            elif token_type == "MULTIPLY":
                self.parse_multiplication()
            elif token_type == "DIVIDE":
                self.parse_division()
            elif token_type == "SQUARE":
                self.parse_square()
            elif token_type == "WRITE":
                self.parse_write()
            elif token_type == "READ":
                self.parse_read()
            elif token_type == "AND":
                self.parse_and()
            elif token_type == "OR":
                self.parse_or()
            elif token_type == "XOR":
                self.parse_xor()
            elif token_type == "NOT":
                self.parse_not()
            elif token_type == "COMMENT":
                self.advance()
            else:
                raise SyntaxError("Unexpected token: {}".format(value))

    def parse_variable_declaration(self):
        self.advance()  # Move past "VAR"
        variable_name = self.current_token[1]
        self.advance()  # Move past identifier
        self.advance()  # Move past "="
        value = int(self.current_token[1])
        self.variables[variable_name] = value
        #print("Variable '{}' declared with value {}".format(variable_name, value))
        self.advance()

    def parse_addition(self):
        self.advance()  # Move past "ADD"
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance()  # Move past first operand
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 + var2
        print("Addition: {} + {} = {}".format(var1, var2, result))
        # Update the variable's value in the dictionary
        self.variables[var2_name] = result
        self.advance()

    def parse_subtraction(self):
        self.advance()  # Move past "SUB"
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance()  # Move past first operand
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 - var2
        #print("Subtraction: {} - {} = {}".format(var1, var2, result))
        # Update the variable's value in the dictionary
        self.variables[var2_name] = result
        self.advance()

    def parse_multiplication(self):
        self.advance()  # Move past "MULTIPLY"
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance()  # Move past first operand
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 * var2
        #print("Multiplication: {} * {} = {}".format(var1, var2, result))
        # Update the variable's value in the dictionary
        self.variables[var2_name] = result
        self.advance()

    def parse_division(self):
        self.advance()  # Move past "DIVIDE"
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance()  # Move past first operand
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 / var2
        #print("Division: {} / {} = {}".format(var1, var2, result))
        # Update the variable's value in the dictionary
        self.variables[var2_name] = result
        self.advance()

    def parse_square(self):
        self.advance()  # Move past "SQUARE"
        var_name = self.current_token[1]
        var = self.variables[var_name]
        result = var ** 2
        #print("Square: {} * {} = {}".format(var, var, result))
        # Update the variable's value in the dictionary
        self.variables[var_name] = result
        self.advance()

    def parse_write(self):
        self.advance()  # Move past "WRITE"
        token_type, value = self.current_token
        if token_type == "STRING":
            print(value.strip('"'))  # Print the string without quotes
        elif token_type == "IDENTIFIER":
            # If the token is an identifier, print the value of the variable
            var_name = value
            var_value = self.variables.get(var_name)
            if var_value is not None:
                print(var_value)
            else:
                print("Undefined variable: {}".format(var_name))
        else:
            raise SyntaxError("Invalid token for WRITE: {}".format(value))
        self.advance()  # Move to the next token

    def parse_read(self):
        self.advance()  # Move past "READ"
        var_name = self.current_token[1]
        user_input = input()
        self.variables[var_name] = user_input
        self.advance()
    
    def parse_and(self):
        self.advance()  # Move past "AND"
        # Parse operands
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance()  # Move past first operand
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 & var2
        # Update variable value
        self.variables[var2_name] = result
        print("AND Operation: {} | {} = {}".format(var1, var2, result))
        self.advance()

    def parse_or(self):
        self.advance()  # Move past "OR"
        # Parse operands
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance()  # Move past first operand
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 | var2
        # Update variable value
        self.variables[var2_name] = result
        print("OR Operation: {} | {} = {}".format(var1, var2, result))
        self.advance()

    def parse_xor(self):
        self.advance()  # Move past "XOR"
        # Parse operands
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance()  # Move past first operand
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 ^ var2
        # Update variable value
        self.variables[var2_name] = result
        print("XOR Operation: {} | {} = {}".format(var1, var2, result))
        self.advance()

    def parse_not(self):
        self.advance()  # Move past "NOT"
        var_name = self.current_token[1]
        var = self.variables[var_name]
        result = ~var
        # Update variable value
        self.variables[var_name] = result
        print("NOT Operator: {} = {}".format(var, result))
        self.advance()

    def parse_factorization(self):
        self.advance()  # Move past "FACTORIZE"
        var_name = self.current_token[1]
        num = self.variables[var_name]
        factors = self.factorize(num)
        print("Factors of {}: {}".format(num, factors))
        self.advance()

    def factorize(self, num):
        factors = []
        # Start with the smallest prime factor (2)
        divisor = 2
        while divisor * divisor <= num:
            while num % divisor == 0:
                factors.append(divisor)
                num //= divisor
            divisor += 1
        if num > 1:
            factors.append(num)
        return factors