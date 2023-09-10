#version 330 core

// number of lights for multiple light
//#define NR_POINT_LIGHTS 2

// Outputs colors in RGBA
out vec4 FragColor;

// Imports the current position from the Vertex Shader
in vec3 crntPos;
// Imports the normal from the Vertex Shader
in vec3 Normal;
// Imports the color from the Vertex Shader
in vec3 color;
// Imports the texture coordinates from the Vertex Shader
in vec2 texCoord;
// Imports that is rendering for edge or not
in float isEdge;


// Gets the Texture Units from the main function
uniform sampler2D diffuse0;
// Specular Texture
//uniform sampler2D specular0;
// Gets the color of the light from the main function
uniform vec4 lightColor;
// Gets the position of the light from the main function
uniform vec3 lightPos;
// Gets the position of the camera from the main function
uniform vec3 camPos;


// For Multiple light
//vec4 pointLight(vec3 lightPos)

vec4 pointLight()
{	
	// used in two variables so I calculate it here to not have to do it twice
	vec3 lightVec = lightPos - crntPos;

	// intensity of light with respect to distance
	float dist = length(lightVec);
	float a = 3.0;
	float b = 0.7;
	//float inten = 1.0f / (a * dist * dist + b * dist + 1.0f);
	float inten = 1.0f / (1.0 + 0.09f * dist + b * dist + 0.032f * dist * dist);

	// ambient lighting
	float ambient = 0.30f;

	// diffuse lighting
	vec3 normal = normalize(Normal);
	vec3 lightDirection = normalize(lightVec);
	float diffuse = max(dot(normal, lightDirection), 0.0f);

	// specular lighting
	float specularLight = 0.90f;
	vec3 viewDirection = normalize(camPos - crntPos);
	vec3 reflectionDirection = reflect(-lightDirection, normal);
	float specAmount = pow(max(dot(viewDirection, reflectionDirection), 0.0f), 51.2f);
	float specular = specAmount * specularLight;
	vec4 initColor = texture(diffuse0, texCoord);

	if (initColor.a<0.99){
		ambient = 0.80f;
		float ratio = 1.00 / 1.52;
		vec3 I = normalize(crntPos - camPos);
		vec3 R = refract(I,normal, ratio);
		return vec4((initColor * (diffuse * inten + ambient +specular*10.0 * inten)).rgb,initColor.a);
	}
	else{
		// Rending solid rings without transparency
		ambient = 1.2f;
		vec4 rings =(texture(diffuse0, texCoord) * (diffuse * inten + ambient +specular*1.0 * inten));
		return vec4(rings.xyz,1.0f);
	}
}

void main()
{
	// For Multiple light
	//vec4 result=vec4(0.0);
	//for(int i = 0; i < NR_POINT_LIGHTS; i++){
	//	//lightPos = lightsPos[i];
	//	result += pointLight(lightsPos[i]);    
	//}
	
	// Without edges just uncomment this line and comment all after
	//FragColor = pointLight();

	// Drawing point in sicular shape
	//float dist = length(gl_PointCoord  - vec2(0.5));
    //float alpha = smoothstep(0.5, 0.55, dist);
	//if (dist > 0.5)
    //   discard;
    //FragColor = vec4(1.0, 0.0, 0.0, 1.0-alpha);
    //FragColor = vec4(pointLight().x,pointLight().y,pointLight().z, 1.0-alpha);
    //FragColor = vec4(pointLight().x,pointLight().y,pointLight().z, pointLight().a*(1.0-alpha));
	//FragColor = pointLight();

	vec4 result = pointLight();
	if (isEdge == 1.0){
		if (result.a < 1.0){
			FragColor = vec4(result.xyz+0.3,result.a);
			//FragColor = vec4(0.0,0.0,0.0,1.0);
			//FragColor = vec4(vec3(0.0),1.0);
			//FragColor = pointLight();
			}
		else
			// Dose not draw edge for rings
			discard;
	}
	else
		FragColor = pointLight();
}