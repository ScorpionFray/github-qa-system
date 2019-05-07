class User:
    field = ''
    name = ''
    followers = 0
    following = 0
    mail = ''
    region = ''
    repositories = 0
    stars = 0
    homepage = ''

    def __init__(self,ans_str):
        if(ans_str=="init"):
            field = ''
            name = ''
            followers = 0
            following = 0
            mail = ''
            region = ''
            repositories = 0
            stars = 0
            homepage = ''
            return
        ################################ 字符区 ##############################
        pos = ans_str.find("field")
        while ans_str[pos] != "'" :
            pos = pos + 1
        pos = pos + 1
        while ans_str[pos] != "'" :
            self.field = self.field + ans_str[pos]
            pos = pos + 1

        pos = ans_str.find("name")
        while ans_str[pos] != "'" :
            pos = pos + 1
        pos = pos + 1
        while ans_str[pos] != "'" :
            self.name = self.name + ans_str[pos]
            pos = pos + 1

        pos = ans_str.find("mail")
        while ans_str[pos] != "'" :
            pos = pos + 1
        pos = pos + 1
        while ans_str[pos] != "'" :
            self.mail = self.mail + ans_str[pos]
            pos = pos + 1

        pos = ans_str.find("region")
        while ans_str[pos] != "'" :
            pos = pos + 1
        pos = pos + 1
        while ans_str[pos] != "'" :
            self.region = self.region + ans_str[pos]
            pos = pos + 1
        pos = ans_str.find("homepage")
        while ans_str[pos] != "'" :
            pos = pos + 1
        pos = pos + 1
        while ans_str[pos] != "'" :
            self.homepage = self.homepage + ans_str[pos]
            pos = pos + 1
    ################################## 数字区 ##############################
        pos = ans_str.find("followers")
        while (ans_str[pos] < '0' or ans_str[pos]> '9') :
            pos = pos + 1
        while (ans_str[pos] >= '0' and ans_str[pos] <= '9'):
            self.followers = self.followers * 10 + int(ans_str[pos])
            pos = pos + 1

        pos = ans_str.find("following")
        while (ans_str[pos] < '0' or ans_str[pos]> '9') :
            pos = pos + 1
        while (ans_str[pos] >= '0' and ans_str[pos] <= '9'):
            self.following = self.following * 10 + int(ans_str[pos])
            pos = pos + 1

        pos = ans_str.find("repositories")
        while (ans_str[pos] < '0' or ans_str[pos]> '9') :
            pos = pos + 1
        while (ans_str[pos] >= '0' and ans_str[pos] <= '9'):
            self.repositories = self.repositories * 10 + int(ans_str[pos])
            pos = pos + 1

        pos = ans_str.find("stars")
        while (ans_str[pos] < '0' or ans_str[pos]> '9') :
            pos = pos + 1
        while (ans_str[pos] >= '0' and ans_str[pos] <= '9'):
            self.stars = self.stars * 10 + int(ans_str[pos])
            pos = pos + 1
    def clean(self):
        field = ''
        name = ''
        followers = 0
        following = 0
        mail = ''
        region = ''
        repositories = 0
        stars = 0
        homepage = ''
    def ans_phase(self):
        return "It's " + self.name + ",click the home buttom to visit his homepage"