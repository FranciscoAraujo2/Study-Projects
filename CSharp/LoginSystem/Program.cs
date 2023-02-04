using System;

namespace Login
{
    class Program
    {
        static void Main(string[] args)
        {
            // Access the global variables for username and password
            Console.WriteLine("\nRegister Account\n");

            // Register System
            Console.WriteLine("Enter your name");
            var name = Console.ReadLine();

            Console.WriteLine("Enter your password");
            var password = Console.ReadLine();

            Console.WriteLine("\nAccount registered successfully\n");
            
            //Login System
            Console.WriteLine("Enter your name");
            var name2 = Console.ReadLine();

            Console.WriteLine("Enter your password");
            var password2 = Console.ReadLine();

            // Check if the entered username and password match the predefined values
            if (name2 + password2 == name + password)
            {
                Console.WriteLine("\nLogin successful\n");
            }
            else{
                Console.WriteLine("\nLogin failed\n");
            }

        }
    }
}
