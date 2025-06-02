public class NavigationSystem
{
    private Robot _robot;
    private bool _isInitialized = false;
    private bool _isEnabled = false;
    
    // Simple map representation
    private List<string> _mapLog = new List<string>();
    
    public NavigationSystem(Robot robot)
    {
        _robot = robot;
    }
    
    public void Initialize()
    {
        if (_isInitialized) return;
        
        Console.WriteLine("Initializing navigation system...");
        _mapLog.Add("System initialized at origin point (0,0)");
        _isInitialized = true;
        Console.WriteLine("Navigation system initialized.");
    }
    
    public void Enable()
    {
        if (!_isInitialized) throw new InvalidOperationException("Navigation system not initialized");
        
        Console.WriteLine("Enabling navigation system...");
        _isEnabled = true;
        Console.WriteLine("Navigation system enabled.");
    }
    
    public void Disable()
    {
        Console.WriteLine("Disabling navigation system...");
        _isEnabled = false;
        Console.WriteLine("Navigation system disabled.");
    }
    
    public void UpdateMap(Dictionary<SensorArray.SensorType, double> sensorData)
    {
        if (!_isEnabled) return;
        
        string entry = $"Navigation update at {DateTime.Now:T}: ";
        foreach (var data in sensorData)
        {
            entry += $"{data.Key}={data.Value:0.00}; ";
        }
        
        _mapLog.Add(entry);
    }
    
    public void DisplayMap()
    {
        Console.WriteLine("=== Navigation Map ===");
        foreach (var entry in _mapLog)
        {
            Console.WriteLine(entry);
        }
    }
    
    public void CalculatePathTo(int x, int y)
    {
        if (!_isEnabled) return;
        
        Console.WriteLine($"Calculating path to coordinates ({x},{y})");
        // In a real system, this would use pathfinding algorithms
        Console.WriteLine("Path calculation complete (simulated)");
    }
}
