from django.template import Variable, VariableDoesNotExist
from django.template.context import Context

def resolve_variable(variable,  context,  default = None):
    if not variable[0] == variable[-1] == '"':
        try:
            resolved_variable = Variable(variable).resolve(context)
        except VariableDoesNotExist:
            if default == None:
                resolved_variable = None
            else:
                resolved_variable = default
    else:
        resolved_variable = str(variable[1:-1])
    return resolved_variable

def combine_variable_list(args_list, context):
    sum = ''
    for arg in args_list:
        sum = sum + str(resolve_variable(arg, context, arg))
    return sum

def copy_context(context):
    new_context = Context(dict_ = context)
    return new_context