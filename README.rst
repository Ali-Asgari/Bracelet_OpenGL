===========
Bracelet in OpenGL
===========

A simple template for fast implementation of OpenGL, GLAD, and GLFW in C++. It includes useful functions for handling Buffers, Textures, lights, drawing object with edges or points, camera movement, blending and more. Additionally consist of comprehensive GLSL programs to facilitate the learning process.\
Utilized Python programs to generate vertecies information include position, color, texture coordinate. 

Result:
-----

.. image:: https://github.com/Ali-Asgari/Bracelet_OpenGL/blob/main/result.gif


Before blending:
-----

.. image:: https://github.com/Ali-Asgari/Bracelet_OpenGL/blob/main/before_blending.png



After enabling of blending and set alpha value for jewels

GLSL codes:

.. code-block:: c++

	if (initColor.a<0.99){
		ambient = 0.80f;
		float ratio = 1.00 / 1.52;
		vec3 I = normalize(crntPos - camPos);
		vec3 R = refract(I,normal, ratio);
		return vec4((initColor * (diffuse * inten + ambient +specular*10.0 * inten)).rgb,initColor.a);
	}

Enable blending and blend function codes:

.. code-block:: c++


	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);



After blending and before drawing edges:
-----
.. image:: https://github.com/Ali-Asgari/Bracelet_OpenGL/blob/main/before_edge.png


GLSL codes:

.. code-block:: c++

	if (isEdge == 1.0){
		if (result.a < 1.0){
			FragColor = vec4(result.xyz+0.3,result.a);
		}
		else{
			// Dose not draw edge for rings
			discard;
        }
    }


render edges of jewels codes:

.. code-block:: c++

    glUniform1f(glGetUniformLocation(shader.ID, "uisEdge"), 1.0);
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    glDrawElements(GL_TRIANGLES, indices.size(), GL_UNSIGNED_INT, 0);
    
After drawing edges:
-----
.. image:: https://github.com/Ali-Asgari/Bracelet_OpenGL/blob/main/after_edge.png


.. code-block:: c++
    glUniform1f(glGetUniformLocation(shader.ID, "uisEdge"), 1.0);
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    glDrawElements(GL_TRIANGLES, indices.size(), GL_UNSIGNED_INT, 0);




Usage
-----

Open solution file in Visual Studio or compile it with terminal.
