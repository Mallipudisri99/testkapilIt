document.addEventListener('DOMContentLoaded', () => {
    const cursor = document.createElement('div');
    cursor.classList.add('cursor');
    document.body.appendChild(cursor);
  
    const follower = document.createElement('div');
    follower.classList.add('cursor', 'cursor__follower');
    document.body.appendChild(follower);
  
    // Store the initial scroll position
    let scrollX = 0;
    let scrollY = 0;                        
  
    document.addEventListener('mousemove', (e) => {
      setPosition(follower, e, scrollX, scrollY);
      setPosition(cursor, e, scrollX, scrollY); 
    });
  
    // Update the scroll position when the user scrolls
      window.addEventListener('scroll', () => {
      scrollX = window.scrollX;
      scrollY = window.scrollY;   
    });
  
      function setPosition(element, e, scrollX, scrollY){
      element.style.transform = `translate3d(${e.clientX + scrollX}px, ${e.clientY + scrollY}px, 0)`;
    }
  });
  
  /*------      */
  document.querySelector('#contact-form').addEventListener('submit', (e) => {
      e.preventDefault();
      e.target.elements.name.value = '';
      e.target.elements.email.value = '';
      e.target.elements.message.value = '';
    });
  
  
  
  