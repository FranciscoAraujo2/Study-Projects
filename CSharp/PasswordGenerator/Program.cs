using System;
using System.Security.Cryptography;

namespace PasswordGenerator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Length: ");
            // Read the password length from the console
            string input = Console.ReadLine();
            int length;
            // Attempt to convert the input to an integer
            if (int.TryParse(input, out length))
            {
                // Call the GeneratePassword method and store the result in the password variable
                string password = GeneratePassword(length);
                Console.WriteLine("Generated password: " + password);
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a valid integer.");
            }
        }

        public static string GeneratePassword(int length)
        {
            // String of valid characters for the password
            const string validChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
            // Create a new instance of the Random class
            Random random = new Random();
            // Array to store the generated password
            char[] chars = new char[length];
            // Loop to generate each character in the password
            for (int i = 0; i < length; i++)
            {
                // Select a random character from the validChars string
                chars[i] = validChars[random.Next(validChars.Length)];
            }
            // Return the generated password as a string
            return new string(chars);
        }
    }
}
