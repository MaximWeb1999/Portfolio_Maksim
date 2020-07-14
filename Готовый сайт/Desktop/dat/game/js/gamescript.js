    	
                var questions = new Array (
                'человек, занимающийся паркуром', 
                'название кувырков в паркуре', 
                'прыжок на объект с места',
                'основатель паркура',
                'первая команда трейсеров',
                'прыжок на стену с хватом за ее верхний край', 
                'бег вдоль по вертикальной стене',
                'комбинация залезания на стену и прыжка', 
                'активный прыжок на низкую поверхность',
                'преодоление препятствий прыжком с помощью рук', 
                'родственный паркуру спорт «для зрителя»',
                'профессия, в которой пригодится паркур',
                'эффективное преодоление преград в городе',
                'прохождение препятствия на руках',
                'перелет через препятствие со сменой руки', 
                'боковое сальто с одной ноги в группировке') 
                var answers = new Array   (
                'трейсер', 'роллы', 'accuracy', 'Давид Белль', 'Yamakasi', 'Cat leap', 'Wallrun', 'тик-так', 'дроп', 'ваулт', 'фриран', 'спасатель', 'паркур', 'Cat pass', 'лэйзи','арабское')

    	    	for (var i=0;i<10000;i++)	{ //10000 раз перемешиваем
    	    		var first = Math.floor(Math.random(1)*15)
    	    		var second = Math.floor(Math.random(1)*15)
    	    		var temp1 = questions[first]
    	    		questions[first] = questions[second]
    	    		questions[second] = temp1
    	    		var temp2 = answers[first]
    	    		answers[first] = answers[second]
    	    		answers[second] = temp2
    	    	}
    	    	var united = new Array() //общий массив с 6 парами
    	    	for (var i=0;i<6;i++) 
    	    		united.push(questions[i],answers[i]) //+ пары
    	    	for (var i=0;i<10000;i++)	{ //10000 раз перемешиваем
    	    		var first = Math.floor(Math.random(1)*12)
    	    		var second = Math.floor(Math.random(1)*12)
    	    		var temp1 = united[first]
    	    		united[first] = united[second]
    	    		united[second] = temp1
    	    	}

function main(id0) {
    	    		count++
    	    		if (count==1) {    	    			
    	    			document.getElementById(id0).style.backgroundImage='radial-gradient( white, rgba(255,140,0,.9))'
    	    			try1=document.getElementById(id0).innerHTML
    	    			id1=id0 
    	    		}
					if (count==2) {
    	    			try2=document.getElementById(id0).innerHTML
    	    			var right = false
    	    			for (var k=0;k<6;k++)	{
    	    				if ((try1==questions[k] && try2==answers[k])||(try2==questions[k] && try1==answers[k]) )
    	    						right = true
    	    				}
    	    			if (right==true) {
    	    				document.getElementById(id0).style.backgroundImage='radial-gradient( white, rgba(255,140,0,.9))'
    	    				document.getElementById(id0).className += " hidden"
    	    				document.getElementById(id1).className += " hidden"
                            good++
                            if (good==6) {
                                document.getElementById('pan0').className = " panel"
                                document.getElementById('pan0').innerHTML='Поздравляем! <br>Ваш промокод на бесплатное занятие:<br>PAR'+(Math.round(Math.random(1)*1000)*11+30000)
                            }
    	    			}
                        else {
                            document.getElementById(id1).style.backgroundImage='radial-gradient( white, rgba(190,225,255,0.9))'
                            if (id1!=id0)
                            bad++   
                        }
                        count=0
                        document.getElementById('r').innerHTML=good
                        document.getElementById('w').innerHTML=bad
                        document.getElementById('res').innerHTML=
                        Math.round(good/(good+bad+0.0000001)*100)+'%'
    	    		}
}