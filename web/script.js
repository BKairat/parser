async function js_cmd_to_py(country){
   document.getElementById('result').innerHTML = "<p>Processing...</p>";
   let res = await eel.get_inform(country)();
   document.getElementById('result').innerHTML = res;
}