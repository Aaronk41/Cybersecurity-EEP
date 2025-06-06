public class Robot
{
    public string Name { get; private set; }
    public bool IsPoweredOn { get; private set; }
    public bool IsEmergencyStopped { get; private set; }
    

    public MotorController MotorController { get; private set; }
    public SensorArray Sensors { get; private set; }
    public NavigationSystem Navigation { get; private set; }
    
    public Robot(string name)
    {
        Name = name;
        MotorController = new MotorController();
        Sensors = new SensorArray();
        Navigation = new NavigationSystem(this);
    }
    
    public void Initialize()
    {
        Console.WriteLine($"{Name} initializing...");
        
      
        MotorController.Initialize();
        Sensors.Initialize();
        Navigation.Initialize();
        
        IsPoweredOn = true;
        IsEmergencyStopped = false;
        
        Console.WriteLine($"{Name} initialized successfully.");
    }
    
    public void Start()
    {
        if (IsEmergencyStopped)
        {
            Console.WriteLine("Cannot start - emergency stop is active. Reset first.");
            return;
        }
        
        Console.WriteLine($"{Name} starting...");
        MotorController.Enable();
        Sensors.Enable();
        Navigation.Enable();
        
        Console.WriteLine($"{Name} is ready.");
    }
    
    public void Stop()
    {
        Console.WriteLine($"{Name} stopping...");
        
       
        Navigation.Disable();
        Sensors.Disable();
        MotorController.Disable();
        
        IsPoweredOn = false;
        Console.WriteLine($"{Name} stopped.");
    }
    
    public void EmergencyStop()
    {
        Console.WriteLine($"EMERGENCY STOP ACTIVATED FOR {Name}!");
        IsEmergencyStopped = true;
        MotorController.EmergencyStop();
        Sensors.Disable();
        Navigation.Disable();
    }
    
    public void ResetEmergencyStop()
    {
        if (!IsEmergencyStopped) return;
        
        Console.WriteLine($"Resetting emergency stop for {Name}");
        IsEmergencyStopped = false;
        Initialize();
    }
    

    public void MoveForward(int durationMs)
    {
        if (!IsPoweredOn || IsEmergencyStopped) return;
        
        Console.WriteLine($"Moving forward for {durationMs}ms");
        MotorController.SetMotorSpeeds(0.5, 0.5);
        Thread.Sleep(durationMs);
        MotorController.StopAll();
    }
    
    public void MoveBackward(int durationMs)
    {
        if (!IsPoweredOn || IsEmergencyStopped) return;
        
        Console.WriteLine($"Moving backward for {durationMs}ms");
        MotorController.SetMotorSpeeds(-0.3, -0.3);
        Thread.Sleep(durationMs);
        MotorController.StopAll();
    }
    
    public void TurnLeft(int degrees)
    {
        if (!IsPoweredOn || IsEmergencyStopped) return;
        
        Console.WriteLine($"Turning left {degrees}°");
        MotorController.SetMotorSpeeds(-0.3, 0.3);
        
        Thread.Sleep(degrees * 10); 
        MotorController.StopAll();
    }
    
    public void TurnRight(int degrees)
    {
        if (!IsPoweredOn || IsEmergencyStopped) return;
        
        Console.WriteLine($"Turning right {degrees}°");
        MotorController.SetMotorSpeeds(0.3, -0.3);
        
        Thread.Sleep(degrees * 10); 
        MotorController.StopAll();
    }
    
    public void ScanEnvironment()
    {
        if (!IsPoweredOn || IsEmergencyStopped) return;
        
        Console.WriteLine("Scanning environment...");
        var scanResults = Sensors.PerformScan();
        
        Console.WriteLine("Scan results:");
        foreach (var result in scanResults)
        {
            Console.WriteLine($"- {result.Key}: {result.Value}");
        }
        
        Navigation.UpdateMap(scanResults);
    }
}
