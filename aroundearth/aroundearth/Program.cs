namespace aroundearth
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            // vaja arvutada, mitu kahe eurost münti läheb ümber maa
            // ,aa ümbermõõt, tuleb välja arvutada raadius abil

            double coinDiameter = 25.75; //mm
            double eartRadius = 6378000000; //mm

            double maaÜmber = 2 * Math.PI * eartRadius;

            double vastus = maaÜmber / coinDiameter;
            Console.WriteLine("vaja läheb " + vastus);
        }
    }
}
