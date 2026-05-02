void main() {}

class Calculator {
  int addition({required int num1, required int num2}) {
    var total = num1 + num2;
    return total;
  }

  int substraction({required int num1, required int num2}) {
    var total = num1 + num2;
    return total;
  }

  dynamic division({required int num1, required int num2}) {
    if (num2 != 0) {
      var total = num1 / num2;
      return total;
    } else {
      return "can't divide by zero[0]";
    }
  }

  int multiplication({required int num1, required int num2}) {
    var total = num1 * num2;
    return total;
  }
}
