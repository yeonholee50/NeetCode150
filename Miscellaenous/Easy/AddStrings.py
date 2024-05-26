class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        mapping = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
        }
        number1 = 0
        counter = 1
        for i in range(len(num1) - 1, -1, -1):
            number1+=(mapping[num1[i]] * counter)
            counter*=10
        number2 = 0
        counter = 1
        for i in range(len(num2) - 1, -1, -1):
            number2+=(mapping[num2[i]] * counter)
            counter*=10
        summation = number1 + number2
        reverse_mapping = {
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            0: "0",
        }
        
        res = ""
        while summation != 0:
            n = summation % 10
            res = res + reverse_mapping[n]
            summation = summation // 10
        return res[::-1] if res != "" else "0"