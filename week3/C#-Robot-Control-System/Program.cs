using System;
using System.Threading;

namespace RobotControlSystem
{
    public class Program
    {
        public static void Main(string[] args)
        {
        
            var robot = new Robot("R2-D2");
            
            try
            {
             
                robot.Initialize();
                robot.Start();
                
                
                RunDemo(robot);
                
             
                robot.Stop();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Robot error: {ex.Message}");
                robot.EmergencyStop();
            }
        }
        
        private static void RunDemo(Robot robot)
        {
            
            robot.MoveForward(1000);  // Move forward for 1 second
            robot.TurnRight(90);      // Turn 90 degrees right
            robot.MoveForward(500);   // Move forward for 0.5 seconds
            robot.ScanEnvironment(); // Perform environment scan
        }
    }
}
