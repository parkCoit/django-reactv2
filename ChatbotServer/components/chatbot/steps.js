export default [
	{
		id: '1',
		message: '안녕하세요 {name}',
		trigger: '2',
	},
	{
		id: '2',
		message: '손잡이 QR코드를 찍어주세요 ?',
		trigger: '3',
	},
	{
		id: '3',
		user: true,
		trigger: '4',
	},
	
	{
		id: '4',
		message: ' 사용전 우산내부 사진을 찍어서 올려주세요 ',
		trigger: '5',
	},
	{
		id: '5',
		message: '대여가 시작됩니다. 시작시간은 10:10입니다. ',
		end: true,
	}
];