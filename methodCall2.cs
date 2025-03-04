namespace methodCall2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            // siin kasutad if ja else 
            // mõlemaks valikuks peab välja kutsuma meetodi
            // teemaks paaris ja paartu arvud
            // paaris ja paritu arvu tekst in teise meetodi sees


//EvenNumber meetod

            Console.WriteLine("Hello, World!");

            int number = int.Parse(Console.ReadLine());

            if (int.IsEvenInteger(number))
            {
                EvenNumber(number);
            }
            else
            {
                oddNumber(number);
            }

            static void EvenNumber(int nr)
            {
                Console.WriteLine("tegemist on paaris arvuga" + nr);
            }


            
//oddNumber meetod

            static void oddNumber(int nr)
            {
                Console.WriteLine("tegemist on paaris arvuga" + nr);
            }
            

        }
    }
}
