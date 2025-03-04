namespace koduTöö
{
       internal class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("Sisesta esimene arv:");
            double arv1 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Sisesta teine arv:");
            double arv2 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Vali tehe (+, -, *, /):");
            char mark = Convert.ToChar(Console.ReadLine());

            double tulemus;

            if (mark == '+')
            {
                tulemus = arv1 + arv2;
                Console.WriteLine("Tulemus: " + tulemus);
            }
            else if (mark == '-')
            {
                tulemus = arv1 - arv2;
                Console.WriteLine("Tulemus: " + tulemus);
            }
            else if (mark == '*')
            {
                tulemus = arv1 * arv2;
                Console.WriteLine("Tulemus: " + tulemus);
            }
            else if (mark == '/')
            {
                if (arv2 != 0)
                {
                    tulemus = arv1 / arv2;
                    Console.WriteLine("Tulemus: " + tulemus);
                }
                else
                {
                    Console.WriteLine("Bum bum oled nulliga ei saa jagada! ");
                }
            }
            else
            {
                Console.WriteLine("Vale tehe!");
            }



        }
        

    }

}