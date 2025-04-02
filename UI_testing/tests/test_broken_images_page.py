
def test_broken_image_page(broken_image_page):
    broken_images = [broken_image_page.image1, broken_image_page.image2, broken_image_page.image3]
    for image in broken_images:
        natural_width = broken_image_page.get_image_natural_width(image)
        if image == broken_image_page.image1 or image == broken_image_page.image2:
            assert natural_width == 0, f"Expected image to be broken, but found naturalWidth: {natural_width}"
        else:
            assert natural_width > 0, f"Expected image to be not broken, but found naturalWidth: {natural_width}"
