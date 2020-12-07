#Newtons Method

def apply_newtons_method(X_before):
    #Formulas:
    #f(x) = x^3 - x - 1
    #f'(x) = 3x^2 - 1
    #Solve for function value
    X_function_value = (X_before ** 3) - (X_before) - 1
    #Solve for derivative value
    X_derivative_value = (3 * (X_before ** 2)) - 1
    quotient = X_function_value/X_derivative_value
    
    return X_before - quotient

def compare_values(X_before, X_after):
    #Allows us to compare numbers up to 6 decimal places
    X_before_str = str(X_before)
    X_after_str = str(X_after)
    #Separates decimal values from integer values
    X_before_comparison = X_before_str.split('.')
    X_after_comparison = X_after_str.split('.')
    if X_after_comparison[0] != X_before_comparison[0] or X_after_comparison[1][0:7] != X_before_comparison[1][0:7]:
        return True
    else:
        return False
X_1 = float(input("Please enter the first value for x: "))
#Primarily going to be X_1, value changes as loop iterates
X_before = X_1 

#Apply newtons method
X_after = apply_newtons_method(X_before)

#list of values of X until closest value is found
X_list = []

run = compare_values(X_before, X_after)

while run:
    X_list.append(X_before)
    X_before = X_after
    X_after = apply_newtons_method(X_before)
    run = compare_values(X_before, X_after)
 
#append answer as last value of list
X_list.append(X_before)
X_after = apply_newtons_method(X_before)
X_list.append(X_after)

for index, value in enumerate(X_list, start=1):
    if(index != len(X_list)):
        print("X{}: {}".format(index, value))
    else:
        print("X{}: {} <- answer".format(index, value))
