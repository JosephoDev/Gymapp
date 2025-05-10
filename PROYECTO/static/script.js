document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("registerForm");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const fullname = document.getElementById("fullname").value;
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirm_password").value;

        // Validación de contraseña
        if (password !== confirmPassword) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Las contraseñas no coinciden.',
            });
            return;
        }

        // Crea un objeto FormData con los datos del formulario
        const formData = new FormData();
        formData.append("name", fullname);  // 'name' es el campo esperado en el backend
        formData.append("password", password);

        try {
            const response = await fetch("/register", {
                method: "POST",
                body: formData // Usa FormData aquí
            });

            const result = await response.json();

            if (response.ok) {
                Swal.fire({
                    icon: 'success',
                    title: 'Registro exitoso',
                    text: result.message
                }).then(() => {
                    window.location.href = '/login';  // Redirige al login si todo va bien
                });
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: result.detail || "No se pudo registrar el usuario."
                });
            }

        } catch (error) {
            console.error("Error:", error);
            Swal.fire({
                icon: 'error',
                title: 'Error de red',
                text: 'No se pudo conectar con el servidor.'
            });
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("login");

    form.addEventListener("submit", async function (e) {
        e.preventDefault(); // Evita el envío por defecto del formulario

        const username = document.getElementById("name").value.trim();
        const password = document.getElementById("psw").value;

        // Validación: el nombre de usuario solo puede contener letras mayúsculas y minúsculas
        const usernamePattern = /^[a-zA-Z\s]+$/;


        if (!usernamePattern.test(username)) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'El nombre de usuario solo puede contener letras mayúsculas y minúsculas.',
            });
            return;
        }

        if (username.length === 0) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'El nombre de usuario no puede estar vacío.',
            });
            return;
        }

        try {
            // Crear un FormData con los datos del formulario
            const formData = new FormData();
            formData.append("name", username);
            formData.append("password", password);

            // Hacer una solicitud POST al backend para verificar las credenciales
            const response = await fetch("/login", {
                method: "POST",
                body: formData
            });

            const result = await response.json();

            if (response.ok) {
                Swal.fire({
                    icon: 'success',
                    title: 'Inicio de sesión exitoso',
                    text: result.message
                });

                setTimeout(() => {
                    window.location.href = '/home';
                }, 2000);

            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error de inicio de sesión',
                    text: result.error || "Usuario o contraseña incorrectos."
                });
            }
        } catch (error) {
            console.error("Error:", error);
            Swal.fire({
                icon: 'error',
                title: 'Error de red',
                text: 'No se pudo conectar con el servidor.'
            });
        };

    });

});