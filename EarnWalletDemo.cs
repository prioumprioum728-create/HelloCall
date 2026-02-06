using System;
using System.IO;
using System.Text.Json;

class EarnWalletDemo
{
    static void Main()
    {
        // Read system_numbers_earn.json
        string jsonText = File.ReadAllText("system_numbers_earn.json");
        JsonDocument doc = JsonDocument.Parse(jsonText);

        string projectNumber = doc.RootElement.GetProperty("project_number").GetString();
        string packageName = doc.RootElement.GetProperty("app_package").GetString();

        Console.WriteLine("📦 App Package: " + packageName);
        Console.WriteLine("🔢 Project Number: " + projectNumber);
        Console.WriteLine("----------------------------------");

        // Demo wallet (NO real money)
        int coins = 0;
        bool freeTrialUsed = false;

        // Free Trial
        if (!freeTrialUsed)
        {
            coins += 500;
            freeTrialUsed = true;
            Console.WriteLine("🎉 Free Trial Activated!");
        }

        // Earn coins
        coins += 20;
        Console.WriteLine("💰 Earned 20 coins");

        // Spend coins
        coins -= 10;
        Console.WriteLine("💸 Spent 10 coins");

        Console.WriteLine("----------------------------------");
        Console.WriteLine("🪙 Final Balance: " + coins + " Coins");
        Console.WriteLine("⚠️ Demo only — no real money used");
    }
}
