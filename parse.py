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
            elif token_type == "PLUS":
                self.parse_addition()
            elif token_type == "MINUS":
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
            elif token_type == "FACT":
                self.parse_factorization()
            elif token_type == "IsPRIME":
                self.parse_is_prime()
            elif token_type == "PPRIME":
                self.parse_print_prime()
            elif token_type == "COMMENT":
                self.advance()
            else:
                raise SyntaxError("Unexpected token: {}".format(value))

    def parse_variable_declaration(self):
        self.advance() 
        variable_name = self.current_token[1]
        self.advance()  
        self.advance() 
        value = int(self.current_token[1])
        self.variables[variable_name] = value
        #print("Variable '{}' declared with value {}".format(variable_name, value))
        self.advance()

    def parse_addition(self):
        self.advance()  
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance() 
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 + var2
        print("Addition: {} + {} = {}".format(var1, var2, result))
        self.variables[var2_name] = result
        self.advance()

    def parse_subtraction(self):
        self.advance() 
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance() 
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 - var2
        #print("Subtraction: {} - {} = {}".format(var1, var2, result))
        self.variables[var2_name] = result
        self.advance()

    def parse_multiplication(self):
        self.advance() 
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance() 
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 * var2
        #print("Multiplication: {} * {} = {}".format(var1, var2, result))
        self.variables[var2_name] = result
        self.advance()

    def parse_division(self):
        self.advance() 
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance() 
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 / var2
        #print("Division: {} / {} = {}".format(var1, var2, result))
        self.variables[var2_name] = result
        self.advance()

    def parse_square(self):
        self.advance() 
        var_name = self.current_token[1]
        var = self.variables[var_name]
        result = var ** 2
        #print("Square: {} * {} = {}".format(var, var, result))
        self.variables[var_name] = result
        self.advance()

    def parse_write(self):
        self.advance() 
        token_type, value = self.current_token
        if token_type == "STRING":
            print(value.strip('"')) 
        elif token_type == "IDENTIFIER":
            var_name = value
            var_value = self.variables.get(var_name)
            if var_value is not None:
                print(var_value)
            else:
                print("Undefined variable: {}".format(var_name))
        else:
            raise SyntaxError("Invalid token for WRITE: {}".format(value))
        self.advance() 

    def parse_read(self):
        self.advance() 
        var_name = self.current_token[1]
        user_input = input()
        self.variables[var_name] = user_input
        self.advance()
    
    def parse_and(self):
        self.advance() 
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance() 
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 & var2
        self.variables[var2_name] = result
        print("AND Operation: {} | {} = {}".format(var1, var2, result))
        self.advance()

    def parse_or(self):
        self.advance() 
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance() 
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 | var2
        self.variables[var2_name] = result
        print("OR Operation: {} | {} = {}".format(var1, var2, result))
        self.advance()

    def parse_xor(self):
        self.advance() 
        var1_name = self.current_token[1]
        var1 = self.variables[var1_name]
        self.advance() 
        var2_name = self.current_token[1]
        var2 = self.variables[var2_name]
        result = var1 ^ var2
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
    
    def parse_is_prime(self):
        self.advance()  # Move past "ISPRIME"
        var_name = self.current_token[1]
        num = self.variables[var_name]
        prime = self.is_prime(num)
        if prime:
            print("{} is prime".format(num))
        else:
            print("{} is not prime".format(num))
        self.advance()

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def parse_print_prime(self):
        self.advance()  # Move past "PRINTPRIME"
        limit = int(self.current_token[1])
        prime_numbers = self.get_prime_numbers(limit)
        print("Prime numbers up to {}: {}".format(limit, prime_numbers))
        self.advance()

    def get_prime_numbers(self, limit):
        prime_numbers = []
        for num in range(2, limit + 1):
            if self.is_prime(num):
                prime_numbers.append(num)
        return prime_numbers