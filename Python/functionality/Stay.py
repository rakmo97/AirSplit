

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

        if(not self.original_costs_calculated):
            self.nights_staying_list.append(nights_staying)
            self.name_list.append(name)
            self.num_guests += 1
        else:
            self.nights_staying_list.append(nights_staying)
            self.name_list.append(name)
            self.person_shareprice_list_orig.append(0.0)
            self.num_guests += 1
        
    
    def CalculateOriginalCosts(self, print_summary=True):
        
        self.per_person_cost_each_night_orig = []
        self.num_guests_each_night_orig = []
        self.person_shareprice_list_orig = []
        
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
            
            self.person_shareprice_list_orig.append(this_guest_cost)
                
        # Check if sums to total price
        if (abs(sum(self.person_shareprice_list_orig) - self.total_price) > 1e3 ):
            raise Warning('Per person pricing does not sum to total price. Check if there is a night nobody is staying...')
            
            
        self.original_costs_calculated = True
        if(print_summary):
            print("===========================================")
            print('Original Price Breakdown Summary:')
            print("Total Price: ${}".format(self.total_price))
            for j in range(self.num_guests):
                print(" - Guest {} is staying {} nights and owes ${:.2f}.".format(self.name_list[j],len(self.nights_staying_list[j]),self.person_shareprice_list_orig[j]))
                
            print("===========================================")
            
        
    def ChangeTotalPrice(self,new_total_price):
        self.total_price = new_total_price
        self.per_night_total_cost = self.total_price/float(self.num_nights);
        
    def ChangePersonNights(self, name="", nights_staying=[]):
        
        index = self.name_list.index(name)       
        self.nights_staying_list[index] = nights_staying
        
        
    def CalculateRedistribution(self, print_summary=True):
        
        if(not self.original_costs_calculated):
            raise AssertionError("Cannot redistribute until original cost breakdown calculated")
        
        self.per_person_cost_each_night_new = []
        self.num_guests_each_night_new = []
        self.person_shareprice_list_new = []
        self.amount_to_send = []
        
        # Calculate per-night cost breakdown        
        for i in range(self.num_nights):
            num_guests_tonight = 0
            
            for j in range(self.num_guests):

                if(i in self.nights_staying_list[j]):
                    num_guests_tonight += 1
                
            per_person_cost_tonight = self.per_night_total_cost / float(num_guests_tonight)

            self.num_guests_each_night_new.append(num_guests_tonight)
            self.per_person_cost_each_night_new.append(per_person_cost_tonight)

        # Calculate per guest cost breakdown
        for j in range(self.num_guests):
            this_guest_cost = 0
            
            for i in range(self.num_nights):
                if(i in self.nights_staying_list[j]):
                    this_guest_cost += self.per_person_cost_each_night_new[i]
            
            self.person_shareprice_list_new.append(this_guest_cost)
                
        # Check if sums to total price
        if (abs(sum(self.person_shareprice_list_new) - self.total_price) > 1e3 ):
            raise Warning('Per person pricing does not sum to total price. Check if there is a night nobody is staying...')
            
            
        self.original_costs_calculated = True
        if(print_summary):
            print("===========================================")
            print('New Price Breakdown Summary:')
            print("Total Price: {}".format(self.total_price))
            for j in range(self.num_guests):
                print(" - Guest {} is staying {} nights and owes ${:.2f}.".format(self.name_list[j],len(self.nights_staying_list[j]),self.person_shareprice_list_new[j]))
                
            print("------------------------------------------")
        
        
        
        for j in range(self.num_guests):
            self.amount_to_send.append(self.person_shareprice_list_new[j]- self.person_shareprice_list_orig[j])
    
        if(print_summary):
            print('\nHow to redistribute:')
            print("Total Price: {}".format(self.total_price))
            for j in range(self.num_guests):
                print(" - Guest {} should {} ${:.2f}.".format(self.name_list[j], "send" if self.amount_to_send[j]>0 else "receive", self.amount_to_send[j]))
                
            print("------------------------------------------")