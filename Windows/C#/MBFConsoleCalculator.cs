using System;
using static System.Console;

namespace MBFConsoleCalculator
{
    internal class Program
    {
        static void Main()
        {
            WriteLine("MBF Calculator");
            WriteLine("Enter the board width in inches:\n");
            var width = ReadLine();

            WriteLine("Enter the board height in inches:\n");
            var height = ReadLine();

            WriteLine("Enter the board length in feet:\n");
            var length = ReadLine();

            var dimensions = ConvertToDoubleArray(width, height, length);
            WriteLine($"MBF: {GetMBF(dimensions)}");
            ReadLine();
        }

        public static double[] ConvertToDoubleArray(
            string width, string height, string length)
        {
            try
            {
                var dimensions = new double[3]
                {
                    double.Parse(width),
                    double.Parse(height),
                    double.Parse(length)
                };

                return dimensions;
            }
            catch (FormatException ex)
            {
                WriteLine($"{ex.Message}\nPlease enter numbers only");
                ReadLine();
                return new double[0];
            }
        }

        public static double GetMBF(double[] dimensions)
        {
            double result = 1;
            foreach (double dim in dimensions)
            {
                result *= dim;
            }
            result /= 144;
            return result;
        }
    }
}
