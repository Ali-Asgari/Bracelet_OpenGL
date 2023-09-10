#include "Mesh.h"

Mesh::Mesh(std::vector <Vertex>& vertices, std::vector <GLuint>& indices, std::vector <Texture>& textures)
{
	Mesh::vertices = vertices;
	Mesh::indices = indices;
	Mesh::textures = textures;

	VAO.Bind();
	// Generates Vertex Buffer Object and links it to vertices
	VBO VBO(vertices);
	// Generates Element Buffer Object and links it to indices
	EBO EBO(indices);
	// Links VBO attributes such as coordinates and colors to VAO
	VAO.LinkAttrib(VBO, 0, 3, GL_FLOAT, sizeof(Vertex), (void*)0);
	VAO.LinkAttrib(VBO, 1, 3, GL_FLOAT, sizeof(Vertex), (void*)(3 * sizeof(float)));
	VAO.LinkAttrib(VBO, 2, 3, GL_FLOAT, sizeof(Vertex), (void*)(6 * sizeof(float)));
	VAO.LinkAttrib(VBO, 3, 2, GL_FLOAT, sizeof(Vertex), (void*)(9 * sizeof(float)));
	// Unbind all to prevent accidentally modifying them
	VAO.Unbind();
	VBO.Unbind();
	EBO.Unbind();
}


void Mesh::Draw(Shader& shader, Camera& camera)
{

	//glBufferData(GL_ARRAY_BUFFER, vertices.size() * sizeof(Vertex), vertices.data(), GL_STATIC_DRAW);


	// Bind shader to be able to access uniforms
	shader.Activate();
	VAO.Bind();

	// Keep track of how many of each type of textures we have
	unsigned int numDiffuse = 0;
	unsigned int numSpecular = 0;

	for (unsigned int i = 0; i < textures.size(); i++)
	{
		std::string num;
		std::string type = textures[i].type;
		if (type == "diffuse")
		{
			num = std::to_string(numDiffuse++);
		}
		else if (type == "specular")
		{
			num = std::to_string(numSpecular++);
		}
		textures[i].texUnit(shader, (type + num).c_str(), i);
		textures[i].Bind();
	}
	// Take care of the camera Matrix
	glUniform3f(glGetUniformLocation(shader.ID, "camPos"), camera.Position.x, camera.Position.y, camera.Position.z);
	camera.Matrix(shader, "camMatrix");


	//Some good functions for draw
	//glEnable(GL_PROGRAM_POINT_SIZE);
	//glHint(GL_POINT_SMOOTH_HINT, GL_NICEST);
	//glsmoo
	//glDrawElements(GL_LINE_STRIP, indices.size(), GL_UNSIGNED_INT, 0);
	//glDisable(GL_PROGRAM_POINT_SIZE);
	//glEnable(GL_POLYGON_OFFSET_FILL);
	//glPolygonOffset(1, 1);
	
	// Draw front and back face
	//glCullFace(GL_FRONT_AND_BACK);


	// Draw the actual mesh
	glUniform1f(glGetUniformLocation(shader.ID, "uisEdge"), 0.0);
	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
	glDrawElements(GL_TRIANGLES, indices.size(), GL_UNSIGNED_INT, 0);
	glLineWidth(2.0f);

	// Drawing a line on the edges of dimond and ...
	glUniform1f(glGetUniformLocation(shader.ID, "uisEdge"), 1.0);
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
	glDrawElements(GL_TRIANGLES, indices.size(), GL_UNSIGNED_INT, 0);
	
	// Drawing points
	//glDrawArrays(GL_POINTS, 0, indices.size());
}