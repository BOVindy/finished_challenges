"""A Claim has the following properties:

ClaimID, ClaimType, Description, ClaimAmount, DateOfIncident, DateOfClaim, IsValid

Komodo allows an insurance claim to be made up to 30 days after an incident
took place.  If the claim is not in the proper time limit, it is not valid.

A ClaimType could be the following:
	Car, Home, Theft

Choose a menu item:
1. See all claims
2. Take care of next claimself.claimid = last_idself.claimid = last_id
3. Enter a new claim
"""
last_id = 0

class Claim:
    def __init__(self, claimtype, description, claimamount, dateofincident, dateofclaim, isvalid):
        global last_id
        last_id += 1
        self.claimid = last_id
        self.claimtype = claimtype
        self.description = description
        self.claimamount = claimamount
        self.dateofincident = dateofincident
        self.dateofclaim = dateofclaim
        self.isvalid = isvalid

    def __repr__(self):
        return f"{SELF---claim.id}, {claim.claimtype}, {claim.claimtype}, {claim.description}, {claim.claimamount}, {claim.dateofincident}, {claim.dateofclaim}, {claim.isvalid}"

class Claims_bag:
    def __init__(self):
        self.claims_list = []

    def return_claims(self):
        return self.claims_list

    def removeclaim(self, tempclaim_id):
        try:
            tempclaim_id = int(tempclaim_id)
            for claim in self.claims_list:
                if tempclaim_id == claim.claimid:
                    self.claims_list.remove(claim)
                    print("claim has been taken care of")
                    break
                else:
                    print("this claim_id does not exist in the database")
        except:
            print("please enter a valid badge_id")

    def addclaim(self, claimtype, description, claimamount, dateofincident, dateofclaim, isvalid):
        newclaim = Claim(claimtype, description, claimamount, dateofincident, dateofclaim, isvalid)
        self.claims_list.append(newclaim)

class Menu:
    def __init__(self):
        self.claimmenu = Claims_bag()
        self.choices = {
            "1": self.show_claims,
            "2": self.add_claim,
            "3": self.remove_claim,
            "4": exit
        }

    def display_menu(self):
        print(
            """
            Claims Menu:
            1. Show all claims
            2. add claim
            3. remove claim
            4. exit
            """
        )

    def run(self):
        while True:
            self.display_menu()
            choice = input("enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")


    def show_claims(self, claims=None):
        if not claims:
            claims = self.claimmenu.return_claims()
            for claim in claims:
                print(f"{claim.claimtype}, {claim.description}, {claim.claimamount}, {claim.dateofincident}, {claim.dateofclaim}, {claim.isvalid}")

    def add_claim(self):
        while True:
            claimtype = input("please enter claim claimtype: (car, home, theft) \n > ")
            if claimtype in ["car", "home", "theft"]:
                break
            else:
                print("please enter a valid claim claimtype. ex(car, home, theft) \n ")


        description = input("please enter a claim description \n > ")

        while True:
            claimamount = input("please enter the amount of the claim (in euros): \n > ")
            try:
                claimamount = float(claimamount)
                print("modded to float")
                break
            except:
                print("please enter a correct amount in euros. ex(1.00, 3000.00) \n ")

        dateofincident = input("please enter the date of the incident (day/month/year) \n> ")

        dateofclaim = input("please enter the date that the claim was filed on (day/month/year) \n> ")

        self.claimid = last_id

        while True:
            isvalid = input("is the claim valid? (yes or no)\n > ").lower()
            if isvalid in ["yes", "no"]:
                break
            else:
                print("invalid entry claimtype, please enter yes or no \n")

        self.claimmenu.addclaim(claimtype, description, claimamount, dateofincident, dateofclaim, isvalid)

        print("your claim has been added.")

    def remove_claim(self):
        tempclaim_id = input("what is the claim_id of the claim that you would like to remove: \n> ")
        self.claimmenu.removeclaim(tempclaim_id)

if __name__ == "__main__":
    menu = Menu()
    menu.run()

