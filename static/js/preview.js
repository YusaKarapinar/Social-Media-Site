function previewImage(event) {
    const file = event.target.files[0];
    const previewContainer = document.getElementById("image-preview-container");

    if (file && file.type.startsWith("image/")) {
        const reader = new FileReader();
        reader.onload = (e) => {
            previewContainer.innerHTML = `<img src="${e.target.result}" alt="Resim Önizlemesi" class="image-preview-item">`;
        };
        reader.readAsDataURL(file);
    } else {
        previewContainer.innerHTML = "";
        alert("Sadece resim dosyalarını yükleyebilirsiniz.");
    }
}
