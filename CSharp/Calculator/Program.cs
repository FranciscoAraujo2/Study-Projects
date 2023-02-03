using System;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            // Print the calculator menu
            Console.WriteLine("Simple Calculator");
            Console.WriteLine("1. Addition");
            Console.WriteLine("2. Subtraction");
            Console.WriteLine("3. Multiplication");
            Console.WriteLine("4. Division");
            Console.WriteLine("Choose an option:");

            // Read the user's choice
            int choice = Convert.ToInt32(Console.ReadLine());

            // Read the first number
            Console.WriteLine("Enter the first number:");
            double num1 = Convert.ToDouble(Console.ReadLine());

            // Read the second number
            Console.WriteLine("Enter the second number:");
            double num2 = Convert.ToDouble(Console.ReadLine());

            double result = 0;

            // Perform the calculation based on the user's choice
            switch (choice)
            {
                case 1:
                    // Addition
                    result = num1 + num2;
                    break;
                case 2:
                    // Subtraction
                    result = num1 - num2;
                    break;
                case 3:
                    // Multiplication
                    result = num1 * num2;
                    break;
                case 4:
                    // Division
                    result = num1 / num2;
                    break;
                default:
                    Console.WriteLine("Invalid option");
                    break;
            }

            // Print the result
            Console.WriteLine("Result: " + result);

            // Wait for the user to press enter
            Console.ReadLine();
        }
    }
}
