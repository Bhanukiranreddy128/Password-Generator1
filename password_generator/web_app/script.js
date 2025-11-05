function getRandomValues(length) {
  const array = new Uint32Array(length);
  window.crypto.getRandomValues(array);
  return array;
}

function generatePassword(length, sets) {
  if (sets.length === 0) throw new Error("Select at least one character set.");
  const all = sets.join('');
  const vals = getRandomValues(length);
  let pwd = '';
  for (let i = 0; i < length; i++) {
    pwd += all[vals[i] % all.length];
  }
  return pwd;
}

document.getElementById('gen').addEventListener('click', () => {
  const length = parseInt(document.getElementById('length').value, 10) || 16;
  const sets = [];
  if (document.getElementById('upper').checked) sets.push('ABCDEFGHIJKLMNOPQRSTUVWXYZ');
  if (document.getElementById('lower').checked) sets.push('abcdefghijklmnopqrstuvwxyz');
  if (document.getElementById('digits').checked) sets.push('0123456789');
  if (document.getElementById('symbols').checked) sets.push('!@#$%^&*()_+[]{}|;:,.<>?');
  try {
    const pwd = generatePassword(length, sets);
    document.getElementById('password').value = pwd;
  } catch (e) {
    alert(e.message);
  }
});

document.getElementById('copy').addEventListener('click', async () => {
  const pwd = document.getElementById('password').value;
  if (!pwd) return;
  try {
    await navigator.clipboard.writeText(pwd);
    alert('Copied to clipboard');
  } catch (e) {
    alert('Copy failed: ' + e);
  }
});
