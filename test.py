

"""if __name__ == '__main__':
    async def main():
        a = FileService(".")
        f = a.get("tEst_fuck_man").unwrap()
        print((await f.content).unwrap()[0])

    run(main())
"""


"""class Fuck:
    string = "fuck"

    def a(self):
        class Me:
            string = "me"

            def b(sf):
                print(self.string)
        return Me()


Fuck().a().b()"""


class A:
    def suicide(self):
        del self.__class__
        print("aaa")

    def test(self):
        print(self)


a = A()
a.suicide()
a.test()