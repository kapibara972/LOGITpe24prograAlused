namespace ifelse
{
    internal class Program
    
        static void Main(string[] args)
        {


            // if ja else rakendus tuleb teha 
            //kontrollib sinu vanus
            // 1. kui oled alla 18, siis konsool annab vastuseks " et oled alaealine"
            // 2. kui oled 19 kuni  65 aastat vana, siis konsool vastab " et oled täisealine"
            // 3. ku oled üle 65  a ´van´, siis pensionäär




            Console.WriteLine("kui vana oled");
            int vanus = int.Parse(Console.ReadLine());

            if (vanus < 18)
                Console.WriteLine("oled alaealine");

            else if (vanus >= 18 && vanus <= 64)
                Console.WriteLine("oled täiskasvand ");

            else if (vanus >= 65)
                Console.WriteLine(" old pensionäär ");
                



        }
    }
}
