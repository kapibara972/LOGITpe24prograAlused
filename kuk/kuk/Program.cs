namespace kuk
{
    internal class Program
    {
        static void Main(string[] args)
        {

            //peab saama sisestada nime 
            // if ja else kontrollib, kas on nimi või on tühi 
            // kui leiate kuskilt teksti värviliseksteha, siis kasutage 
            Console.WriteLine("sisesta nimi");
            string name = Console.ReadLine();

            if (name != "")
            {
                Console.WriteLine("tere" + name);
            }

            else
                {
                Console.WriteLine("EI SISESTAND NIMI");
                 }
        }
    }
}
