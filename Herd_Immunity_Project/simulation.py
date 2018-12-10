import random
import sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''

    def __init__(self, pop_size, vacc_percentage, initial_infected=1, virus=None):
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.logger = Logger("interactions.txt")
        self.population = []  # List of Person objects
        self.pop_size = pop_size  # Int
        self.next_person_id = 0
        self.virus = virus
        self.initial_infected = initial_infected  # Int
        self.total_infected = 0
        self.current_infected = 0
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.newly_infected = []
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, pop_size, vacc_percentage, initial_infected)

    def _create_population(self, initial_infected):
        return self.population
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.
        pass

    def _simulation_should_continue(self):
        while self.pop_size > 0 or not self.vacc_percentage == 1:
            return True
        else:
            return False

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        should_continue = None

        while should_continue:
            # TODO: for every iteration of this loop, call self.time_step() to compute another
            # round of this simulation.
            # print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))
            pass

    def choose_infected(self):
        return random.choice(self.newly_infected)

    def time_step(self):
        rand_infected_person = self.choose_infected()
        rand_person = random.choice(self.population)
        tot_interactions = 0
        while tot_interactions <= 100:
            if not rand_infected_person.is_alive():
                self.choose_infected()
            else:
                self.interaction(rand_person, rand_infected_person)
                tot_interactions += 1

    def interaction(self, person, random_person):
        # Assert statements are to check if
        assert person.is_alive == True
        assert random_person.is_alive == True

        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        if random_person.is_vaccinated():
            pass
        elif random_person.infection == self.virus:
            pass
        elif random_person.is_vaccinated() == False:
            num = random.randint(0, 1)
            if num < self.virus.repro_rate:
                self.newly_infected.append(random_person._id)

            # TODO: Finish this method.d
            #     attribute can be changed to True at the end of the time step.
            # TODO: Call logger method during this method.
        pass

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = list()


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
