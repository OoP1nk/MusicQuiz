# ███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░░██████╗░██╗░░░██╗██╗███████╗
# ████╗░████║██║░░░██║██╔════╝██║██╔══██╗██╔═══██╗██║░░░██║██║╚════██║
# ██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝██║██╗██║██║░░░██║██║░░███╔═╝
# ██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗╚██████╔╝██║░░░██║██║██╔══╝░░
# ██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝░╚═██╔═╝░╚██████╔╝██║███████╗
# ╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝

from data.AccessManager import *

# ---------
# Asks the user what they want to do:
# OPTION1: *Register
# OPTION2: *Login
# OPTION3: *Leaderboard
# ---------
print("1-* Register")
print("2-* Login")
print("3-* Leaderboard")
decision = int(input("Would you like to do?\n"))

# ---------
# Manages the decision made
# ---------
if decision == 1:
    register()
elif decision == 2:
    authorize()
elif decision == 3:
    getLeaderboard()
else:
    print('Unexpected error occurred, please contact an administrator.')
