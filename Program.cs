namespace RandomNumber
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            
            //nüüd tuleb kasutada switchi, et näidata numbrit 1-st kuni 6-1

            
               int number = new Random().Next(1, 6);

            switch (number)
            {
                case 1:
                    Console.WriteLine("veeraetasid nr" + number);
                        break;
                case 2:
                    Console.WriteLine("veeraetasid nr" + number);
                    break;
                case 3:
                    Console.WriteLine("veeraetasid nr" + number);
                    break;
                case 4:
                    Console.WriteLine("veeraetasid nr" + number);
                    break;
                case 5:
                    Console.WriteLine("veeraetasid nr" + number);
                    break;
                case 6:
                    Console.WriteLine("veeraetasid nr" + number);
                    break;


                default:
                    Console.WriteLine(" error ");
                    break;
            }

            

            


        }
    }
}
