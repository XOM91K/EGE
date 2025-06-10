def weather(*args, **kwargs ): # arguments
    print(kwargs)
    return args[0] * kwargs['repeat'], args[1] * kwargs['repeat'], args[2] * kwargs['repeat']
print(weather('8', 'hello', 'tri', repeat=500, end='', sep='|'))