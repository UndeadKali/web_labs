import json


class Solution:

    def sum_number_in_string(self, number_string: str) -> int:
        amountOfInputSymbolsValue = 0
        number_string = number_string
        for element in number_string:
            amountOfInputSymbolsValue += int(element)
        return amountOfInputSymbolsValue

    def get_leader_string(self, steps: int) -> str:
        outputSpruce = ""
        for index in range(steps + 1):
            for j in range(steps - index):
                outputSpruce += " "
            for j in range(index):
                outputSpruce += "#"
            outputSpruce += "\n"
        return outputSpruce

    def to_json(self, func):
        def wrapped(*args, **kwargs):
            return json.dumps(func(*args, **kwargs))

        return wrapped


if __name__ == '__main__':

    solution = Solution()
    solution.sum_number_in_string('12345')
    # 15
    solution.sum_number_in_string('160438521039')
    # 42

    solution = Solution()
    print(solution.get_leader_string(3))

    print(solution.get_leader_string(5))


    @solution.to_json
    def get_data():
        return {
            'data': 42
        }


    get_data()
