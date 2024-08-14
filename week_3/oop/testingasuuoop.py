import asuu as a

board_member=a.AsuuBody("president obi","vice_president","secretary")

board_member.mouth="mouth"
board_member.hand="hand"
board_member.leg="leg"
board_member.eye="eye"



board_member.secretary="executive secretary"

print(board_member.can_talk())
print(board_member.secretary)
print(board_member.can_declare_strike())