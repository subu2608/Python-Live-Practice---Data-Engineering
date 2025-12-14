class Employee:
    companyname="Google"

    @classmethod
    def replace_company_name(cls,replace):
        cls.companyname=replace

    @staticmethod
    def tryreplace_company_name(replace2):
        companyname=replace2

c=Employee()
print("Before Replcament: ", c.companyname)
Employee.companyname="OpenAI"
print("After Class method Replacement:", Employee.companyname)
Employee.tryreplace_company_name("Perplexity")
print("After static method:", Employee.companyname)
