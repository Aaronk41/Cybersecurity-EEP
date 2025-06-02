public class MotorController
{
    private bool _isInitialized = false;
    private bool _isEnabled = false;
    
    // Motor states (simplified - values between -1.0 and 1.0)
    private double _leftMotorSpeed = 0;
    private double _rightMotorSpeed = 0;
    
    public void Initialize()
    {
        if (_isInitialized) return;
        
        Console.WriteLine("Initializing motor controller...");
        // Simulate hardware initialization
        Thread.Sleep(500);
        _isInitialized = true;
        Console.WriteLine("Motor controller initialized.");
    }
    
    public void Enable()
    {
        if (!_isInitialized) throw new InvalidOperationException("Motor controller not initialized");
        
        Console.WriteLine("Enabling motor controller...");
        _isEnabled = true;
        StopAll();
        Console.WriteLine("Motor controller enabled.");
    }
    
    public void Disable()
    {
        Console.WriteLine("Disabling motor controller...");
        StopAll();
        _isEnabled = false;
        Console.WriteLine("Motor controller disabled.");
    }
    
    public void EmergencyStop()
    {
        Console.WriteLine("Motor controller emergency stop!");
        _leftMotorSpeed = 0;
        _rightMotorSpeed = 0;
        
        _isEnabled = false;
    }
    
    public void SetMotorSpeeds(double left, double right)
    {
        if (!_isEnabled) return;
        
        // Clamp values between -1.0 and 1.0
        _leftMotorSpeed = Math.Clamp(left, -1.0, 1.0);
        _rightMotorSpeed = Math.Clamp(right, -1.0, 1.0);
        
        Console.WriteLine($"Setting motor speeds - Left: {_leftMotorSpeed:0.00}, Right: {_rightMotorSpeed:0.00}");
        
    }
    
    public void StopAll()
    {
        SetMotorSpeeds(0, 0);
    }
    
    public (double left, double right) GetCurrentSpeeds() => (_leftMotorSpeed, _rightMotorSpeed);
}
