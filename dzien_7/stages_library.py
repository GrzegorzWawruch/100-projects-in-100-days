

stage0 = r"""
  +---+
  |   |
      |
      |
      |
      |
      |
========
"""
stage1 = r"""
  +---+
  |   |
  O   |
      |
      |
      |
      |
========
"""
stage2 = r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
      |
========
"""
stage3 = r"""
  +---+
  |   |
  O   |
/ |   |
      |
      |
      |
========
"""
stage4 = r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
      |
========
"""
stage5 = r"""
  +---+
  |   |
  O   |
 /|\  |
  |   |
      |
      |
========
"""
stage6 = r"""
  +---+
  |   |
  O   |
 /|\  |
  |   |
 /    |
      |
========
"""
stage7 = r"""
  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
      |
========
"""
stages = [stage0,stage1,stage2,stage3,stage4,stage5, stage6,stage7]

def player_lives (live):
    print(f'============================== You use {live}/7 lives ===================')