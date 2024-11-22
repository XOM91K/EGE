import sys
import signal
import keyboard
#
# class PasswordError(ValueError):
#     pass
#
#
# class LengthError(PasswordError):
#     pass
#
#
# class LetterError(PasswordError):
#     pass
#
#
# class DigitError(PasswordError):
#     pass
#
#
# class SequenceError(PasswordError):
#     pass
#
#
# def check_password(a):
#     count = 0
#     alp = 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэёячсмитьбю'
#     digi = '1234567890!@#$%^&*()_+-=.,/?|:;><{}[]'
#     letters = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
#                'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
#     digits = list('1234567890')
#     for v in a.lower():
#         if v not in alp and v not in digi:
#             return 'error'
#     if len(a) < 9:
#         raise LengthError('LengthError')
#     if a.isupper() or a.islower():
#         raise LetterError('LetterError')
#     if a.isdigit():
#         raise LetterError('LetterError')
#     for z in a:
#         if z not in digits:
#             count += 1
#     if count == len(a):
#         raise DigitError('DigitError')
#     low_a = a.lower()
#     for i in letters:
#         for _ in range(len(i) - 2):
#             if i[_: _ + 3] in low_a:
#                 raise SequenceError('SequenceError')
#     for num in digits:
#         if num in a:
#             return 'ok'
#     else:
#         raise DigitError('DigitError')
#
#
# def signal_handler(sig, frame):
#     print("Bye-Bye")
#     sys.exit(0)
#
#
#
#
# while True:
#     try:
#         print(signal.signal(signal.SIGINT, signal_handler))
#         password_input = input()
#         print(signal.SIGINT)
#         if password_input == 'Ctrl+Break':
#             signal_handler(None, None)
#         result = check_password(password_input)
#         if result == 'ok':
#             print(result)
#             break
#         else:
#             print(result)
#     except KeyboardInterrupt:
#         print("Bye-Bye")
#         sys.exit(0)
#     except LengthError as e:
#         print(e.__class__.__name__)
#     except LetterError as e:
#         print(e.__class__.__name__)
#     except DigitError as e:
#         print(e.__class__.__name__)
#     except SequenceError as e:
#         print(e.__class__.__name__)
#     except Exception as e:
#         print(e.__class__.__name__)
# keyboard.on_press(key_board_event)
# def key_board_event(event):
#     print("Нажата клавиша: ")
# keyboard.wait('esc')