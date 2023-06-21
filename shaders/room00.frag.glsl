#version 150

uniform vec3 iResolution;
uniform float iTime;
uniform float iTimeDelta;
uniform float iFrameRate;
uniform int iFrame;
uniform float iChannelTime[4];
uniform vec3 iChannelResolution[4];
uniform vec4 iMouse;
uniform sampler2D iChannel0;
uniform sampler2D iChannel1;
uniform sampler2D iChannel2;
uniform sampler2D iChannel3;
uniform vec4 iDate;

in vec2 texcoord;
out vec4 fragColor;

void main() {
    vec2 p = texcoord * iResolution.xy;
    
    // Set position
    vec2 v = iResolution.xy;
    p = (p - v * 0.5) * 1.0 / v.y;
    
    // Trippy breathing effect
    p += p * sin(dot(p, p) * 2.0 - sin(iTime)) * 0.001;
    
    // Convert to 3D
    vec3 q = vec3(p, 0.0);
    
    // Accumulate color
    vec4 c = vec4(0.0);
    for (float i = 0.5; i < 10.0; i++) {
        
        // Fractal formula and rotation
        q.xy = sin(abs(2.0 * fract(q.xy - vec2(0.5)) - 1.0)) * mat2(cos(0.02 * (iTime + iMouse.x * 0.1) * i * i + 0.78 * vec4(1.0, 7.0, 3.0, 1.0)));
        q.z += 0.2;
        
        // Coloration
        float colorIndex = mod(iTime * 5.0 + i * 0.5, 10.0);
        vec3 color = vec3(0.0);
        
        if (colorIndex < 1.0)
            color = vec3(1.0, 0.0, 0.0);
        else if (colorIndex < 2.0)
            color = vec3(0.0, 1.0, 0.0);
        else if (colorIndex < 3.0)
            color = vec3(0.0, 0.0, 1.0);
        else if (colorIndex < 4.0)
            color = vec3(1.0, 1.0, 0.0);
        else if (colorIndex < 5.0)
            color = vec3(1.0, 0.0, 1.0);
        else
            color = vec3(0.0, 1.0, 1.0);
        
        // Trippy color effect
        c.rgb += exp(-abs(sin(iTime) * q.y) * 5.0) * color;
    }
    
    // Set alpha component to 0.2
    c.a = 0.2;
    
    // Adjust colors
    c *= 0.2;
    c *= 2.0; // Increase the emissive factor here
    
    // Trippy color distortion
    c.r = fract(c.r + sin(iTime) * 0.2);
    c.g = fract(c.g + cos(iTime) * 0.2);
    c.b = fract(c.b + sin(iTime + 1.0) * 0.2);
    
    // Add time-based distortion
    float distortion = sin(iTime) * 0.1;
    c.r += distortion;
    c.g -= distortion;
    c.b += distortion;
    
    fragColor = c;
}
