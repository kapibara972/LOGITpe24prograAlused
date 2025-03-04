namespace oddNumbrs
{
    internal class Program
    {
        static void Main(string[] args)
        {
            
            //komsool küsib numbrit ja siin muudetakse 
            // see int andmetüübiks

            // teha if ja else- ga kontroll
            // kus saame teada, et kas nr
            // on paaris või paaritu 
            // kasuta operaatorit


            Console.WriteLine("ütle number ");
            int number = int.Parse(Console.ReadLine());

            if (number % 2 == 0)
                Console.WriteLine("paaris");

            else
                Console.WriteLine("paaritu");
                


        }
    }
}
