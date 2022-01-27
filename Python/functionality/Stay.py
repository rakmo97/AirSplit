

class Stay:
    
    
    def __init__(self, total_price=1, num_nights=1):
        
        self.total_price = total_price
        self.num_nights = num_nights
        self.name_list = []
        self.nights_staying_list = []
        
        self.per_night_total_cost = total_price/float(num_nights);

        self.original_costs_calculated = False
        self.num_guests = 0
        
    
    def AddPerson(self, name="", nights_staying=[]):
        
        if(any(i in name for i in self.name_list)):
            raise AttributeError("Person {} already added to list. Change name to distinguish.".format(name))
 
        if(not all(y < self.num_nights for y in nights_staying)):
            raise AttributeError("Person {} cannot stay after the {}th night.".format(name, self.num_nights))

        self.nights_staying_list.append(nights_staying)
        self.name_list.append(name)
        self.num_guests += 1
    
    def CalculateOriginalCosts(self, print_summary=True):
        
        self.per_person_cost_each_night_orig = []
        self.num_guests_each_night_orig = []
        self.person_shareprice_list = []
        
        # Calculate per-night cost breakdown        
        for i in range(self.num_nights):
            num_guests_tonight = 0
            
            for j in range(self.num_guests):

                if(i in self.nights_staying_list[j]):
                    num_guests_tonight += 1
                
            per_person_cost_tonight = self.per_night_total_cost / float(num_guests_tonight)

            self.num_guests_each_night_orig.append(num_guests_tonight)
            self.per_person_cost_each_night_orig.append(per_person_cost_tonight)

        # Calculate per guest cost breakdown
        for j in range(self.num_guests):
            this_guest_cost = 0
            
            for i in range(self.num_nights):
                if(i in self.nights_staying_list[j]):
                    this_guest_cost += self.per_person_cost_each_night_orig[i]
            
            self.person_shareprice_list.append(this_guest_cost)
                
        # Check if sums to total price
        if (sum(self.person_shareprice_list) != self.total_price ):
            raise Warning('Per person pricing does not sum to total price. Check if there is a night nobody is staying...')
            
            

        if(print_summary):
            print("===========================================")
            print('Original Price Breakdown Summary:')
            print("Total Price: {}".format(self.total_price))
            for j in range(self.num_guests):
                print(" - Guest {} is staying {} nights and owes ${:.2f}.".format(self.name_list[j],len(self.nights_staying_list[j]),self.person_shareprice_list[j]))
                
            print("===========================================")
            
        
        
        
    def ChangePersonNights(self, guest="", nights_staying):
        
        
        
    # def CalculateRedistribution(self):
        
    
    
