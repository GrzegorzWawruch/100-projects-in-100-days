from turtle import  Turtle

class Snake:
    """Create Snake class.
        Snake is building using blocks"""
    def __init__(self):
        self.blocks = []
        self.create_three_firsts_blocks()
        self.head = self.blocks[0]
        self.block = self.blocks[1]

    def create_three_firsts_blocks(self):
        """This function create three firsts blocks"""
        for i in range(3):
            block=Turtle()
            block.penup()
            block.color("white")
            block.shape("square")
            block.setpos(y = 0, x= (i*(-20)))
            self.blocks.append(block)

    def move_blocks(self):
        """This function move blocks from block_list.
         All blocks except the first one go to the position of the block before it """
        for i in range((len(self.blocks)-1), -1, -1):
            if i > 0:
                self.blocks[i].setpos( x = self.blocks[i-1].xcor() , y = self.blocks[i-1].ycor())

    def turn_left(self):
        """This function turn left head's block"""
        if self.head.heading() != 0:
            self.blocks[0].setheading(180)

    def turn_right(self):
        """This function turn right head's block"""
        if self.head.heading() != 180:
            self.blocks[0].setheading(0)

    def turn_up(self):
        """This function turn up head's block"""
        if self.head.heading() != 270:
            self.blocks[0].setheading(90)

    def turn_down(self):
        """This function turn down head's block"""
        if self.head.heading() != 90:
            self.blocks[0].setheading(270)

    def add_block_to_blocks_list(self):
        """This function add new block to the blocks list"""
        new_block=Turtle()
        new_block.penup()
        new_block.color("white")
        new_block.shape("square")
        if self.head.heading() == 0:
            new_block.setposition(self.blocks[1].xcor()-20, self.blocks[1].ycor())
        if self.head.heading() == 180:
            new_block.setposition(self.blocks[1].xcor()+20, self.blocks[1].ycor())
        if self.head.heading() == 270:
            new_block.setposition(self.blocks[1].xcor(), self.blocks[1].ycor()+20)
        if self.head.heading() == 90:
            new_block.setposition(self.blocks[1].xcor(), self.blocks[1].ycor()-20)
        self.blocks.append(new_block)

    def reset(self):
        for block in self.blocks:
            block.goto(2000,2000)
        self.blocks.clear()
        self.create_three_firsts_blocks()
        self.head = self.blocks[0]