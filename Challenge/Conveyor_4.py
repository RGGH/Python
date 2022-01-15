
# www.redandgreen.co.uk
# Version 0.1.4

# All code in 1 file for ease of email/transfer/test
# I would normally put the large classes into another module

from time import sleep
from random import randint


# Settings
Q_SLOTS = 6 
Q_STEPS = 100  # set to 100 for full trial
DELAY = 0.03  # set to 1 to see 1 step per second if conveyor display is True
DISPLAY = True  # set to True to see "conveyor"
INFO = True  # set to true for full inline logging to screen


class output:
    """capture the products A, B, and completed assemblies for analysis/review"""

    finished_assemblies = 0
    qty_a = 0
    qty_b = 0
    qty_empty = 0


class slots:
    """conveyor belt has 6 empty slots at start"""

    slot_1 = " "
    slot_2 = " "
    slot_3 = " "
    slot_4 = " "
    slot_5 = " "
    slot_6 = " "


class Conveyor:
    """shift the pieces and assmblies 1 step
    each step resets slot 1 with either A or B or empty
    based on 1 out of 3 pseudo random chance
    """

    def add_new_piece(self):

        if randint(0, 2) == 0:
            slots.slot_1 = "A"
            output.qty_a += 1

        elif randint(0, 2) == 1:
            slots.slot_1 = "B"
            output.qty_b += 1
        else:
            slots.slot_1 = "_"
            output.qty_empty += 1

    def display_conveyor(self):

        if DISPLAY == True:

            print("\n---------------------")
            print(
                f" {slots.slot_1}|{slots.slot_2}|{slots.slot_3}|{slots.slot_4}|{slots.slot_5}|{slots.slot_6} "
            )
            print("---------------------")

    def move_conveyor(self):

        slots.slot_6 = slots.slot_5
        slots.slot_5 = slots.slot_4
        slots.slot_4 = slots.slot_3
        slots.slot_3 = slots.slot_2
        slots.slot_2 = slots.slot_1


class Worker:

    """All workers start with empty hands and
    all conveyor slots are empty"""

    def __init__(self, name):

        self.worker_name = name
        self.picker_progress_team_1 = ""
        self.picker_progress_team_2 = ""
        self.picker_progress_team_3 = ""

    # Assume top row  workers get to pick pieces before bottom row workers
    # mark empty slot with 'x' if it had a part on it that was picked off and used

    def pick_part_slot_1(self):
        """workers from either side of slot 1 pick parts and place
        finished assembly back 3 slots further down the conveyor
        """

        while True:

            if slots.slot_1 == "A" and "A" not in self.picker_progress_team_1:
                self.picker_progress_team_1 = self.picker_progress_team_1 + "A"
                print(f"{self.worker_name} picking up a new A")
                slots.slot_1 = "x"

            if slots.slot_1 == "B" and "B" not in self.picker_progress_team_1:
                self.picker_progress_team_1 = self.picker_progress_team_1 + "B"
                print(f"{self.worker_name} picking up a new B")
                slots.slot_1 = "x"

            if (self.picker_progress_team_1 == "AB" or self.picker_progress_team_1 == "BA"):
                print(f"Assembly made:  {self.picker_progress_team_1}")
                slots.slot_1 = "x"
                self.put_assy()
                self.picker_progress_team_1 = ""

            break

    def pick_part_slot_2(self):
        """workers from either side of slot 2 pick parts and place
        finished assembly back 3 slots further down the conveyor
        """

        while True:

            if slots.slot_2 == "A" and "A" not in self.picker_progress_team_2:
                self.picker_progress_team_2 = self.picker_progress_team_2 + "A"
                print(f"{self.worker_name} picking up a new A")
                slots.slot_2 = "x"

            if slots.slot_2 == "B" and "B" not in self.picker_progress_team_2:
                self.picker_progress_team_2 = self.picker_progress_team_2 + "B"
                print(f"{self.worker_name} picking up a new B")
                slots.slot_2 = "x"

            if (self.picker_progress_team_2 == "AB" or self.picker_progress_team_2 == "BA"):
                print(f"Assembly made:  {self.picker_progress_team_2}")
                slots.slot_2 = "x"
                self.put_assy()
                self.picker_progress_team_2 = ""

            break

    def pick_part_slot_3(self):
        """workers from either side of slot 3 pick parts and place
        finished assembly back 3 slots further down the conveyor
        """

        while True:

            if slots.slot_3 == "A" and "A" not in self.picker_progress_team_3:
                self.picker_progress_team_3 = self.picker_progress_team_3 + "A"
                print(f"{self.worker_name} picking up a new A")
                slots.slot_3 = "x"

            if slots.slot_3 == "B" and "B" not in self.picker_progress_team_3:
                self.picker_progress_team_3 = self.picker_progress_team_3 + "B"
                print(f"{self.worker_name} picking up a new B")
                slots.slot_3 = "x"

            if ( self.picker_progress_team_3 == "AB" or self.picker_progress_team_3 == "BA"):
                print(f"Assembly made:  {self.picker_progress_team_3}")
                slots.slot_3 = "x"
                self.put_assy()
                self.picker_progress_team_3 = ""

            break

    def put_assy(self):
        """take the AB or BA assembly and place it 3 slots further down the conveyor belt
        team 1 uses slot 4
        team 2 uses slot 5
        team 3 uses slot 6
        """

        receiving_slot = self.worker_name[1]
        receiving_slot = str(int(receiving_slot) + 3)

        print(f"{self.worker_name} Assembly put into slot {receiving_slot}")

        if self.worker_name[1] == "1":
            slots.slot_4 = "P"
        if self.worker_name[1] == "2":
            slots.slot_5 = "P"
        if self.worker_name[1] == "3":
            slots.slot_6 = "P"

        output.finished_assemblies += 1


# -------------------
# main driver
# -------------------


if __name__ == "__main__":

    if INFO == True:
        
        print("\n\n +++++ Starting conveyor +++++ \n")
        sleep(1)

    Conv = Conveyor()

    """

    t1   t2   t3 
    ---------------------------
    |   |   |   |   |   |    | 
    ---------------------------
    b1   b2   b3

    """

    # create the workers
    t1 = Worker("t1")
    t2 = Worker("t2")
    t3 = Worker("t3")

    b1 = Worker("b1")
    b2 = Worker("b2")
    b3 = Worker("b3")

    # run the conveyor belt
    for i in range(0, Q_STEPS):

        sleep(DELAY)

        Conv.display_conveyor()

        """Assume each pair take from conveyor in equal / random amounts.
        Hint : remove the random, and pair 1, nearest the start 
        of the conveyor will make more assemblies than the others
        *but may want more pay*
        """
        rand = randint(0, 2)
        #
        if rand == 0:
            t1.pick_part_slot_1()
            b1.pick_part_slot_1()
        #
        if rand == 1:
            t2.pick_part_slot_2()
            b2.pick_part_slot_2()
        #
        if rand == 2:
            t3.pick_part_slot_3()
            b3.pick_part_slot_3()

        if INFO == True:
            if i+1 < Q_STEPS:
                print(f"step {i+1} complete > Now moving conveyor and adding a new piece")
            else:
                print(f"step {Q_STEPS} complete - stopped conveyor\n")

        Conv.move_conveyor()
        Conv.add_new_piece()

    # Show final production output
    print("\n\n\tSummary of Production:")
    print("\t------------------------\n")

    print("\t" + "Part A qty " + str(output.qty_a))
    print("\t" + "Part B qty " + str(output.qty_b))
    print("\t" + "Empty Slot qty " + str(output.qty_empty))

    print("\n\tProducts Produced")
    print("\t------------------")
    print("\t" + str(output.finished_assemblies) + "\n")

    print("\n\tMissed Parts")
    print("\t-----------------")
    print("\t" + str(output.qty_a + output.qty_b - (2 * output.finished_assemblies)) + "\n")

    sleep(2)
    print("\n\tThank you\n")

# ------------------------------------------------------
