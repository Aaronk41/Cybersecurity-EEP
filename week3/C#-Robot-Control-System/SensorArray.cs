public class SensorArray
{
    private bool _isInitialized = false;
    private bool _isEnabled = false;
    private Random _random = new Random();
    
    public enum SensorType
    {
        Ultrasonic,
        Infrared,
        Bumper,
        Gyroscope,
        Accelerometer,
        Temperature
    }
    
    public void Initialize()
    {
        if (_isInitialized) return;
        
        Console.WriteLine("Initializing sensor array...");
        
        Thread.Sleep(300);
        _isInitialized = true;
        Console.WriteLine("Sensor array initialized.");
    }
    
    public void Enable()
    {
        if (!_isInitialized) throw new InvalidOperationException("Sensor array not initialized");
        
        Console.WriteLine("Enabling sensor array...");
        _isEnabled = true;
        Console.WriteLine("Sensor array enabled.");
    }
    
    public void Disable()
    {
        Console.WriteLine("Disabling sensor array...");
        _isEnabled = false;
        Console.WriteLine("Sensor array disabled.");
    }
    
    public Dictionary<SensorType, double> PerformScan()
    {
        if (!_isEnabled) return new Dictionary<SensorType, double>();
        
        var results = new Dictionary<SensorType, double>();
        
       
        if (_isEnabled)
        {
            results.Add(SensorType.Ultrasonic, _random.NextDouble() * 5);
            results.Add(SensorType.Infrared, _random.NextDouble());
            results.Add(SensorType.Bumper, 0); 
            results.Add(SensorType.Gyroscope, _random.NextDouble() * 360); 
            results.Add(SensorType.Accelerometer, _random.NextDouble() * 2); 
            results.Add(SensorType.Temperature, 20 + _random.NextDouble() * 15); 
        }
        
        return results;
    }
    
    public double GetSingleSensorReading(SensorType sensorType)
    {
        if (!_isEnabled) return 0;
        
        return PerformScan()[sensorType];
    }
}
