function calc() {
    			g=document.getElementById('gender').value;
    			w=document.getElementById('weight').value;
    			h=document.getElementById('height').value/100;
    			index = Math.round(w/(h*h)*100)/100;
    			document.getElementById('w_index').innerHTML=index
    			if ((g==0 && index<20) || (g==1 && index<19)) 
    				document.getElementById('verdict').innerHTML= "Дефицит веса. В паркуре будете летать!"
    			else if ((g==0 && index>25) || (g==1 && index>24))
    				document.getElementById('verdict').innerHTML= "Лишний вес. Паркур поможет сбросить!"
    			else 
    				document.getElementById('verdict').innerHTML= "Вес в норме. Паркур - Ваш спорт!"
    		}
            function auth(l,p) {
                if (l=='Автор' && p=='binom') {
                    document.getElementById('greet').innerHTML= 'Привет, Дмитрий!'
                    document.getElementById('logpass').hidden=true
                }
            }
            function rep1(k) {
  					document.getElementById('reply1').innerHTML=''
  					age0=document.getElementById('age').value
  					if (age0)
  						document.getElementById('reply1').innerHTML='У нас есть занятия паркуром для '+age0+'-летних!<br>'
  					if (k)	
  						document.getElementById('reply1').innerHTML += r[k]
  				}
  				var q=new Array('Мне интересны занятия паркуром ','Интересно, но не устраивает расписание','Я еще слишком мал для занятий паркуром','Я уже слишком стар для паркура')
  				var r=new Array('Ждем Вас на занятиях! Позвоните для уточнения расписания. ','Мы можем предложить индивидуальные занятия в удобное для Вас время','Мы занимаемся с детьми от 5 лет! Попроси родителей уточнить.','Занятия с тренером полностью безопасны в любом возрасте!')

                var i = 0
                var images = new Array("slide0","slide1","slide2","slide3")
                function prev(){
                    document.getElementById(images[i]) .className = ""
                    i--
                    if (i < 0) i = images.length - 1 
                    document.getElementById(images[i]) .className = "shown"
                };
                function next(){
                    document.getElementById(images[i]) .className = ""
                    i++
                    if (i > images.length-1) i = 0
                    document.getElementById(images[i]) .className = "shown"
                };