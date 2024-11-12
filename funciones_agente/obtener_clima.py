from selenium.webdriver.common.by import By

def obtener_clima(driver, consulta):
    # Buscar el clima en Google
    driver.get(f"https://www.google.com/search?q=clima+{consulta}")

    try:
        ciudad = driver.find_element(By.CSS_SELECTOR, "span[class='BBwThe']").text
        condicion_climatica = driver.find_element(By.CSS_SELECTOR, "div[class='wob_dcp']").text
        temperatura = driver.find_element(By.CSS_SELECTOR, "span[id='wob_tm']").text
        unidad_temperatura = driver.find_element(By.CSS_SELECTOR, "span[aria-label='°Celsius']").text

        return f"{ciudad}: {condicion_climatica} con {temperatura}{unidad_temperatura}"

    except Exception as e:
        return "No se pudo obtener el clima en este momento."